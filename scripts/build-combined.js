#!/usr/bin/env node

/**
 * Script to build the combined static site locally
 * - Frontend is built to .deploy-local/
 * - Docs is built to .deploy-local/docs
 *
 * Usage:
 *   npm run build-combined
 *   or
 *   node scripts/build-combined.js
 */

import { execSync } from 'node:child_process';
import { existsSync, mkdirSync, cpSync, rmSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = fileURLToPath(new URL('.', import.meta.url));
const ROOT_DIR = resolve(__dirname, '..');
const FRONTEND_DIR = join(ROOT_DIR, 'frontend');
const DOCS_DIR = join(ROOT_DIR, 'docs');
const DEPLOY_DIR = join(ROOT_DIR, '.deploy-local');

console.log('🚀 Building combined static site...\n');

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

  console.log('\n✅ Combined site built successfully!');
  console.log(`   Output directory: ${DEPLOY_DIR}`);
  console.log(`   Frontend: file://${join(DEPLOY_DIR, 'index.html')}`);
  console.log(`   Docs:     file://${join(DEPLOY_DIR, 'docs', 'index.html')}`);
  console.log('\nTo serve locally, run: npm run serve-combined');

} catch (error) {
  console.error('\n❌ Error:', error.message);
  process.exit(1);
}
