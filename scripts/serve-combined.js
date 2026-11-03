#!/usr/bin/env node

/**
 * Script to build and serve the combined static site locally
 * - Frontend is served from /
 * - Docs is served from /docs
 *
 * Usage:
 *   npm run serve-combined
 *   or
 *   node scripts/serve-combined.js
 */

import { execSync } from 'node:child_process';
import { existsSync, mkdirSync, cpSync, rmSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import http from 'node:http';
import { stat, readFile } from 'node:fs/promises';

const __dirname = fileURLToPath(new URL('.', import.meta.url));
const ROOT_DIR = resolve(__dirname, '..');
const FRONTEND_DIR = join(ROOT_DIR, 'frontend');
const DOCS_DIR = join(ROOT_DIR, 'docs');
const DEPLOY_DIR = join(ROOT_DIR, '.deploy-local');

console.log('🚀 Building combined static site for local development...\n');

try {
  // Step 1: Build frontend
  console.log('📦 Building frontend...');
  execSync('npm ci && npm run build', {
    cwd: FRONTEND_DIR,
    stdio: 'inherit'
  });

  // Step 2: Build docs
  console.log('\n📚 Building docs...');
  execSync('npm ci && npm run build', {
    cwd: DOCS_DIR,
    stdio: 'inherit'
  });

  // Step 3: Create combined directory structure
  console.log('\n🗂️  Creating combined directory structure...');

  // Clean up previous deploy directory
  if (existsSync(DEPLOY_DIR)) {
    rmSync(DEPLOY_DIR, { recursive: true, force: true });
  }

  mkdirSync(DEPLOY_DIR, { recursive: true });
  mkdirSync(join(DEPLOY_DIR, 'docs'), { recursive: true });

  // Copy frontend to root
  const frontendDist = join(FRONTEND_DIR, 'dist');
  if (existsSync(frontendDist)) {
    cpSync(frontendDist, DEPLOY_DIR, { recursive: true, dereference: true });
    console.log(`  ✓ Copied frontend from ${frontendDist} to ${DEPLOY_DIR}`);
  } else {
    throw new Error(`Frontend dist directory not found: ${frontendDist}`);
  }

  // Copy docs to /docs
  const docsDist = join(DOCS_DIR, 'dist');
  if (existsSync(docsDist)) {
    cpSync(docsDist, join(DEPLOY_DIR, 'docs'), { recursive: true, dereference: true });
    console.log(`  ✓ Copied docs from ${docsDist} to ${join(DEPLOY_DIR, 'docs')}`);
  } else {
    throw new Error(`Docs dist directory not found: ${docsDist}`);
  }

  // Verify files exist
  console.log('\n📋 Verifying files:');
  const indexPath = join(DEPLOY_DIR, 'index.html');
  const docsIndexPath = join(DEPLOY_DIR, 'docs', 'index.html');

  if (!existsSync(indexPath)) {
    throw new Error(`Frontend index.html not found at ${indexPath}`);
  }
  if (!existsSync(docsIndexPath)) {
    throw new Error(`Docs index.html not found at ${docsIndexPath}`);
  }
  console.log(`  ✓ ${indexPath}`);
  console.log(`  ✓ ${docsIndexPath}`);

  // Step 4: Start a simple HTTP server
  console.log('\n🌐 Starting local server...');
  console.log(`  Frontend: http://localhost:3000`);
  console.log(`  Docs:     http://localhost:3000/docs`);
  console.log(`  Serving from: ${DEPLOY_DIR}`);
  console.log('\nPress Ctrl+C to stop the server\n');

  const server = http.createServer(async (req, res) => {
    const url = new URL(req.url || '/', `http://${req.headers.host || 'localhost'}`);
    let filepath = join(DEPLOY_DIR, url.pathname);

    console.log(`[${new Date().toISOString()}] ${req.method} ${req.url} -> ${filepath}`);

    try {
      let fileStats = await stat(filepath);

      if (fileStats.isDirectory()) {
        // Try to serve index.html
        const indexPath = join(filepath, 'index.html');
        try {
          fileStats = await stat(indexPath);
          if (fileStats.isFile()) {
            filepath = indexPath;
          }
        } catch {
          // No index.html found
          fileStats = null;
        }
      }

      if (fileStats && fileStats.isFile()) {
        const content = await readFile(filepath);
        const ext = filepath.split('.').pop();
        const contentType = {
          html: 'text/html',
          css: 'text/css',
          js: 'application/javascript',
          json: 'application/json',
          png: 'image/png',
          jpg: 'image/jpeg',
          jpeg: 'image/jpeg',
          gif: 'image/gif',
          svg: 'image/svg+xml',
          txt: 'text/plain',
          ico: 'image/x-icon',
          webp: 'image/webp',
          avif: 'image/avif'
        }[ext] || 'application/octet-stream';

        res.writeHead(200, { 'Content-Type': contentType });
        res.end(content);
        return;
      }
    } catch (err) {
      if (err.code === 'ENOENT') {
        // Try with index.html for SPA routing
        try {
          const htmlPath = join(DEPLOY_DIR, url.pathname, 'index.html');
          const htmlStats = await stat(htmlPath);
          if (htmlStats.isFile()) {
            const content = await readFile(htmlPath);
            res.writeHead(200, { 'Content-Type': 'text/html' });
            res.end(content);
            return;
          }
        } catch {
          // Try root index.html for SPA fallback
          try {
            const rootIndex = join(DEPLOY_DIR, 'index.html');
            const rootStats = await stat(rootIndex);
            if (rootStats.isFile()) {
              const content = await readFile(rootIndex);
              res.writeHead(200, { 'Content-Type': 'text/html' });
              res.end(content);
              return;
            }
          } catch {
            // Final fallback: 404
          }
        }
      }
    }

    // 404 Not Found
    console.log(`[${new Date().toISOString()}] 404 ${req.url}`);
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('404 Not Found');
  });

  server.on('error', (err) => {
    console.error('❌ Server error:', err.message);
  });

  server.listen(3000, () => {
    console.log('✅ Server running on http://localhost:3000');
  });

  // Handle cleanup on exit
  process.on('SIGINT', () => {
    console.log('\n🛑 Shutting down server...');
    server.close(() => {
      console.log('✅ Server stopped');
      process.exit(0);
    });
  });

} catch (error) {
  console.error('\n❌ Error:', error.message);
  console.error(error.stack);
  process.exit(1);
}
