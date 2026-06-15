import '@astrojs/internal-helpers/path';
import 'cookie';
import 'kleur/colors';
import 'es-module-lexer';
import { N as NOOP_MIDDLEWARE_HEADER, n as decodeKey } from './chunks/astro/server_BskC6SXv.mjs';
import 'clsx';
import 'html-escaper';

const NOOP_MIDDLEWARE_FN = async (_ctx, next) => {
  const response = await next();
  response.headers.set(NOOP_MIDDLEWARE_HEADER, "true");
  return response;
};

const codeToStatusMap = {
  // Implemented from tRPC error code table
  // https://trpc.io/docs/server/error-handling#error-codes
  BAD_REQUEST: 400,
  UNAUTHORIZED: 401,
  FORBIDDEN: 403,
  NOT_FOUND: 404,
  TIMEOUT: 405,
  CONFLICT: 409,
  PRECONDITION_FAILED: 412,
  PAYLOAD_TOO_LARGE: 413,
  UNSUPPORTED_MEDIA_TYPE: 415,
  UNPROCESSABLE_CONTENT: 422,
  TOO_MANY_REQUESTS: 429,
  CLIENT_CLOSED_REQUEST: 499,
  INTERNAL_SERVER_ERROR: 500
};
Object.entries(codeToStatusMap).reduce(
  // reverse the key-value pairs
  (acc, [key, value]) => ({ ...acc, [value]: key }),
  {}
);

function sanitizeParams(params) {
  return Object.fromEntries(
    Object.entries(params).map(([key, value]) => {
      if (typeof value === "string") {
        return [key, value.normalize().replace(/#/g, "%23").replace(/\?/g, "%3F")];
      }
      return [key, value];
    })
  );
}
function getParameter(part, params) {
  if (part.spread) {
    return params[part.content.slice(3)] || "";
  }
  if (part.dynamic) {
    if (!params[part.content]) {
      throw new TypeError(`Missing parameter: ${part.content}`);
    }
    return params[part.content];
  }
  return part.content.normalize().replace(/\?/g, "%3F").replace(/#/g, "%23").replace(/%5B/g, "[").replace(/%5D/g, "]");
}
function getSegment(segment, params) {
  const segmentPath = segment.map((part) => getParameter(part, params)).join("");
  return segmentPath ? "/" + segmentPath : "";
}
function getRouteGenerator(segments, addTrailingSlash) {
  return (params) => {
    const sanitizedParams = sanitizeParams(params);
    let trailing = "";
    if (addTrailingSlash === "always" && segments.length) {
      trailing = "/";
    }
    const path = segments.map((segment) => getSegment(segment, sanitizedParams)).join("") + trailing;
    return path || "/";
  };
}

function deserializeRouteData(rawRouteData) {
  return {
    route: rawRouteData.route,
    type: rawRouteData.type,
    pattern: new RegExp(rawRouteData.pattern),
    params: rawRouteData.params,
    component: rawRouteData.component,
    generate: getRouteGenerator(rawRouteData.segments, rawRouteData._meta.trailingSlash),
    pathname: rawRouteData.pathname || void 0,
    segments: rawRouteData.segments,
    prerender: rawRouteData.prerender,
    redirect: rawRouteData.redirect,
    redirectRoute: rawRouteData.redirectRoute ? deserializeRouteData(rawRouteData.redirectRoute) : void 0,
    fallbackRoutes: rawRouteData.fallbackRoutes.map((fallback) => {
      return deserializeRouteData(fallback);
    }),
    isIndex: rawRouteData.isIndex
  };
}

function deserializeManifest(serializedManifest) {
  const routes = [];
  for (const serializedRoute of serializedManifest.routes) {
    routes.push({
      ...serializedRoute,
      routeData: deserializeRouteData(serializedRoute.routeData)
    });
    const route = serializedRoute;
    route.routeData = deserializeRouteData(serializedRoute.routeData);
  }
  const assets = new Set(serializedManifest.assets);
  const componentMetadata = new Map(serializedManifest.componentMetadata);
  const inlinedScripts = new Map(serializedManifest.inlinedScripts);
  const clientDirectives = new Map(serializedManifest.clientDirectives);
  const serverIslandNameMap = new Map(serializedManifest.serverIslandNameMap);
  const key = decodeKey(serializedManifest.key);
  return {
    // in case user middleware exists, this no-op middleware will be reassigned (see plugin-ssr.ts)
    middleware() {
      return { onRequest: NOOP_MIDDLEWARE_FN };
    },
    ...serializedManifest,
    assets,
    componentMetadata,
    inlinedScripts,
    clientDirectives,
    routes,
    serverIslandNameMap,
    key
  };
}

const manifest = deserializeManifest({"hrefRoot":"file:///home/erica/Multi/projets/prestagri/prestagri/frontend/","adapterName":"","routes":[{"file":"file:///home/erica/Multi/projets/prestagri/prestagri/frontend/dist/404.html","links":[],"scripts":[],"styles":[],"routeData":{"type":"page","isIndex":false,"route":"/404","pattern":"^\\/404\\/?$","segments":[[{"content":"404","dynamic":false,"spread":false}]],"params":[],"component":"node_modules/@astrojs/starlight/404.astro","pathname":"/404","prerender":true,"fallbackRoutes":[],"_meta":{"trailingSlash":"ignore"}}},{"file":"file:///home/erica/Multi/projets/prestagri/prestagri/frontend/dist/aide_scolarite/index.html","links":[],"scripts":[],"styles":[],"routeData":{"route":"/aide_scolarite","isIndex":false,"type":"page","pattern":"^\\/aide_scolarite\\/?$","segments":[[{"content":"aide_scolarite","dynamic":false,"spread":false}]],"params":[],"component":"src/pages/aide_scolarite.astro","pathname":"/aide_scolarite","prerender":true,"fallbackRoutes":[],"_meta":{"trailingSlash":"ignore"}}},{"file":"file:///home/erica/Multi/projets/prestagri/prestagri/frontend/dist/calcul","links":[],"scripts":[],"styles":[],"routeData":{"route":"/calcul","isIndex":false,"type":"endpoint","pattern":"^\\/calcul\\/?$","segments":[[{"content":"calcul","dynamic":false,"spread":false}]],"params":[],"component":"src/pages/calcul.js","pathname":"/calcul","prerender":true,"fallbackRoutes":[],"_meta":{"trailingSlash":"ignore"}}},{"file":"file:///home/erica/Multi/projets/prestagri/prestagri/frontend/dist/enfant_handicape/index.html","links":[],"scripts":[],"styles":[],"routeData":{"route":"/enfant_handicape","isIndex":false,"type":"page","pattern":"^\\/enfant_handicape\\/?$","segments":[[{"content":"enfant_handicape","dynamic":false,"spread":false}]],"params":[],"component":"src/pages/enfant_handicape.astro","pathname":"/enfant_handicape","prerender":true,"fallbackRoutes":[],"_meta":{"trailingSlash":"ignore"}}},{"file":"file:///home/erica/Multi/projets/prestagri/prestagri/frontend/dist/quotient_familial/index.html","links":[],"scripts":[],"styles":[],"routeData":{"route":"/quotient_familial","isIndex":false,"type":"page","pattern":"^\\/quotient_familial\\/?$","segments":[[{"content":"quotient_familial","dynamic":false,"spread":false}]],"params":[],"component":"src/pages/quotient_familial.astro","pathname":"/quotient_familial","prerender":true,"fallbackRoutes":[],"_meta":{"trailingSlash":"ignore"}}}],"site":"https://doc.prest-agri.beta.gouv.fr/","base":"/","trailingSlash":"ignore","compressHTML":true,"componentMetadata":[["/home/erica/Multi/projets/prestagri/prestagri/frontend/src/pages/aide_scolarite.astro",{"propagation":"none","containsHead":true}],["/home/erica/Multi/projets/prestagri/prestagri/frontend/src/pages/enfant_handicape.astro",{"propagation":"none","containsHead":true}],["/home/erica/Multi/projets/prestagri/prestagri/frontend/src/pages/quotient_familial.astro",{"propagation":"none","containsHead":true}],["\u0000astro:content",{"propagation":"in-tree","containsHead":false}],["/home/erica/Multi/projets/prestagri/prestagri/frontend/node_modules/@astrojs/starlight/404.astro",{"propagation":"in-tree","containsHead":true}],["\u0000@astro-page:node_modules/@astrojs/starlight/404@_@astro",{"propagation":"in-tree","containsHead":false}],["/home/erica/Multi/projets/prestagri/prestagri/frontend/node_modules/@astrojs/starlight/utils/routing.ts",{"propagation":"in-tree","containsHead":false}],["/home/erica/Multi/projets/prestagri/prestagri/frontend/node_modules/@astrojs/starlight/index.astro",{"propagation":"in-tree","containsHead":true}],["\u0000@astro-page:node_modules/@astrojs/starlight/index@_@astro",{"propagation":"in-tree","containsHead":false}],["/home/erica/Multi/projets/prestagri/prestagri/frontend/node_modules/@astrojs/starlight/utils/navigation.ts",{"propagation":"in-tree","containsHead":false}],["/home/erica/Multi/projets/prestagri/prestagri/frontend/node_modules/@astrojs/starlight/components/SidebarSublist.astro",{"propagation":"in-tree","containsHead":false}],["/home/erica/Multi/projets/prestagri/prestagri/frontend/node_modules/@astrojs/starlight/components/Sidebar.astro",{"propagation":"in-tree","containsHead":false}],["\u0000virtual:starlight/components/Sidebar",{"propagation":"in-tree","containsHead":false}],["/home/erica/Multi/projets/prestagri/prestagri/frontend/node_modules/@astrojs/starlight/components/Page.astro",{"propagation":"in-tree","containsHead":false}],["/home/erica/Multi/projets/prestagri/prestagri/frontend/node_modules/@astrojs/starlight/utils/route-data.ts",{"propagation":"in-tree","containsHead":false}],["/home/erica/Multi/projets/prestagri/prestagri/frontend/node_modules/@astrojs/starlight/utils/translations.ts",{"propagation":"in-tree","containsHead":false}],["/home/erica/Multi/projets/prestagri/prestagri/frontend/node_modules/@astrojs/starlight/internal.ts",{"propagation":"in-tree","containsHead":false}],["\u0000virtual:astro-expressive-code/preprocess-config",{"propagation":"in-tree","containsHead":false}],["/home/erica/Multi/projets/prestagri/prestagri/frontend/node_modules/astro-expressive-code/components/renderer.ts",{"propagation":"in-tree","containsHead":false}],["/home/erica/Multi/projets/prestagri/prestagri/frontend/node_modules/astro-expressive-code/components/Code.astro",{"propagation":"in-tree","containsHead":false}],["/home/erica/Multi/projets/prestagri/prestagri/frontend/node_modules/astro-expressive-code/components/index.ts",{"propagation":"in-tree","containsHead":false}],["/home/erica/Multi/projets/prestagri/prestagri/frontend/node_modules/@astrojs/starlight/components.ts",{"propagation":"in-tree","containsHead":false}],["/home/erica/Multi/projets/prestagri/prestagri/frontend/node_modules/@astrojs/starlight/components/Footer.astro",{"propagation":"in-tree","containsHead":false}],["\u0000virtual:starlight/components/Footer",{"propagation":"in-tree","containsHead":false}],["/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/index.mdx",{"propagation":"in-tree","containsHead":false}],["/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/index.mdx?astroPropagatedAssets",{"propagation":"in-tree","containsHead":false}],["/home/erica/Multi/projets/prestagri/prestagri/frontend/node_modules/@astrojs/starlight/user-components/Aside.astro",{"propagation":"in-tree","containsHead":false}],["/home/erica/Multi/projets/prestagri/prestagri/frontend/node_modules/@astrojs/starlight/user-components/FileTree.astro",{"propagation":"in-tree","containsHead":false}]],"renderers":[],"clientDirectives":[["idle","(()=>{var l=(o,t)=>{let i=async()=>{await(await o())()},e=typeof t.value==\"object\"?t.value:void 0,s={timeout:e==null?void 0:e.timeout};\"requestIdleCallback\"in window?window.requestIdleCallback(i,s):setTimeout(i,s.timeout||200)};(self.Astro||(self.Astro={})).idle=l;window.dispatchEvent(new Event(\"astro:idle\"));})();"],["load","(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event(\"astro:load\"));})();"],["media","(()=>{var s=(i,t)=>{let a=async()=>{await(await i())()};if(t.value){let e=matchMedia(t.value);e.matches?a():e.addEventListener(\"change\",a,{once:!0})}};(self.Astro||(self.Astro={})).media=s;window.dispatchEvent(new Event(\"astro:media\"));})();"],["only","(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event(\"astro:only\"));})();"],["visible","(()=>{var l=(s,i,o)=>{let r=async()=>{await(await s())()},t=typeof i.value==\"object\"?i.value:void 0,c={rootMargin:t==null?void 0:t.rootMargin},n=new IntersectionObserver(e=>{for(let a of e)if(a.isIntersecting){n.disconnect(),r();break}},c);for(let e of o.children)n.observe(e)};(self.Astro||(self.Astro={})).visible=l;window.dispatchEvent(new Event(\"astro:visible\"));})();"]],"entryModules":{"\u0000noop-middleware":"_noop-middleware.mjs","\u0000@astro-page:node_modules/@astrojs/starlight/404@_@astro":"pages/404.astro.mjs","\u0000@astro-page:src/pages/aide_scolarite@_@astro":"pages/aide_scolarite.astro.mjs","\u0000@astro-page:src/pages/calcul@_@js":"pages/calcul.astro.mjs","\u0000@astro-page:src/pages/enfant_handicape@_@astro":"pages/enfant_handicape.astro.mjs","\u0000@astro-page:src/pages/quotient_familial@_@astro":"pages/quotient_familial.astro.mjs","\u0000@astro-page:node_modules/@astrojs/starlight/index@_@astro":"pages/_---slug_.astro.mjs","\u0000@astro-renderers":"renderers.mjs","\u0000@astrojs-manifest":"manifest_CaTqc5wP.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/explanation/doc.md?astroContentCollectionEntry=true":"chunks/doc_6-JOPowp.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/index.mdx?astroContentCollectionEntry=true":"chunks/index_VqwRi-3v.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/reference/api.md?astroContentCollectionEntry=true":"chunks/api_DFbHO_Sb.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/reference/contributors.md?astroContentCollectionEntry=true":"chunks/contributors_CXRbJSWy.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/reference/dn.md?astroContentCollectionEntry=true":"chunks/dn_Ckl4jTET.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/reference/note_service.md?astroContentCollectionEntry=true":"chunks/note_service_DNcmuyXs.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/reference/what_did_I_do_then.md?astroContentCollectionEntry=true":"chunks/what_did_I_do_then_C-O7f-NE.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/tutorial/1_first_run.md?astroContentCollectionEntry=true":"chunks/1_first_run_COEi1mE2.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/tutorial/1_staging.md?astroContentCollectionEntry=true":"chunks/1_staging_BmpkrBKP.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/tutorial/catala.md?astroContentCollectionEntry=true":"chunks/catala_DNhRWEFt.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/explanation/doc.md?astroPropagatedAssets":"chunks/doc_BBtF8LmF.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/index.mdx?astroPropagatedAssets":"chunks/index_DIQeLXzZ.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/reference/api.md?astroPropagatedAssets":"chunks/api_DDlQAcNn.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/reference/contributors.md?astroPropagatedAssets":"chunks/contributors_BvsalpJf.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/reference/dn.md?astroPropagatedAssets":"chunks/dn_B0XGs9Uo.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/reference/note_service.md?astroPropagatedAssets":"chunks/note_service_C0qqsXMQ.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/reference/what_did_I_do_then.md?astroPropagatedAssets":"chunks/what_did_I_do_then_chewmoRi.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/tutorial/1_first_run.md?astroPropagatedAssets":"chunks/1_first_run_YqLwvW3S.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/tutorial/1_staging.md?astroPropagatedAssets":"chunks/1_staging_BiEfAGLV.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/tutorial/catala.md?astroPropagatedAssets":"chunks/catala_Cv--y3zU.mjs","\u0000astro:asset-imports":"chunks/_astro_asset-imports_D9aVaOQr.mjs","\u0000astro:data-layer-content":"chunks/_astro_data-layer-content_BcEe_9wP.mjs","\u0000virtual:astro-expressive-code/config":"chunks/config_-pk1mzOb.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/node_modules/astro-expressive-code/dist/index.js":"chunks/index_DaVK51eC.mjs","\u0000virtual:astro-expressive-code/preprocess-config":"chunks/preprocess-config_LodWoUOe.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/explanation/doc.md":"chunks/doc_Bn2df76a.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/index.mdx":"chunks/index_BRVO1Ymc.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/reference/api.md":"chunks/api_CtwIkPkR.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/reference/contributors.md":"chunks/contributors_Bl-ClSIG.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/reference/dn.md":"chunks/dn_CrJqInaW.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/reference/note_service.md":"chunks/note_service_DAC08evh.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/reference/what_did_I_do_then.md":"chunks/what_did_I_do_then_aBK_t1nW.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/tutorial/1_first_run.md":"chunks/1_first_run_CrpO9R2r.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/tutorial/1_staging.md":"chunks/1_staging_CsWbFHJD.mjs","/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/tutorial/catala.md":"chunks/catala_Du1UGLuh.mjs","\u0000virtual:astro-expressive-code/ec-config":"chunks/ec-config_CzTTOeiV.mjs","/astro/hoisted.js?q=0":"_astro/hoisted.Ch1HLGsS.js","/astro/hoisted.js?q=1":"_astro/hoisted.B_N_G3G5.js","/home/erica/Multi/projets/prestagri/prestagri/frontend/node_modules/@astrojs/starlight/user-components/Tabs.astro?astro&type=script&index=0&lang.ts":"_astro/Tabs.astro_astro_type_script_index_0_lang.CCIyraCc.js","astro:scripts/page.js":"_astro/page.7qqag-5g.js","/home/erica/Multi/projets/prestagri/prestagri/frontend/node_modules/@pagefind/default-ui/npm_dist/mjs/ui-core.mjs":"_astro/ui-core.D-anDlNY.js","astro:scripts/before-hydration.js":""},"inlinedScripts":[],"assets":["/_astro/page.7qqag-5g.js","/file:///home/erica/Multi/projets/prestagri/prestagri/frontend/dist/404.html","/file:///home/erica/Multi/projets/prestagri/prestagri/frontend/dist/aide_scolarite/index.html","/file:///home/erica/Multi/projets/prestagri/prestagri/frontend/dist/calcul","/file:///home/erica/Multi/projets/prestagri/prestagri/frontend/dist/enfant_handicape/index.html","/file:///home/erica/Multi/projets/prestagri/prestagri/frontend/dist/quotient_familial/index.html"],"i18n":{"strategy":"pathname-prefix-other-locales","locales":["en"],"defaultLocale":"en","domainLookupTable":{}},"buildFormat":"directory","checkOrigin":false,"serverIslandNameMap":[],"key":"tqUM17yf2G0FbhUB903dK8SxZGU0SM/0rFvzQUbogKU=","experimentalEnvGetSecretEnabled":false});

export { manifest };
