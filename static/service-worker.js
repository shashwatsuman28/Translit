/* Simple service worker for ScriptTranslit PWA */
const CACHE_NAME = 'scripttranslit-v1';
const CORE_ASSETS = [
  './',
  './index.html',
  './manifest.webmanifest'
  // Icons and other static assets can be added here
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(CORE_ASSETS))
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  const { request } = event;
  // Only handle GET
  if (request.method !== 'GET') return;

  event.respondWith(
    caches.match(request).then(cached => {
      if (cached) return cached;
      return fetch(request)
        .then(resp => {
          // Optionally cache fetched responses (basic strategy)
          const copy = resp.clone();
          caches.open(CACHE_NAME).then(cache => {
            cache.put(request, copy).catch(() => { });
          });
          return resp;
        })
        .catch(() => {
          // Offline fallback (could add a custom offline page)
          return caches.match('./index.html');
        });
    })
  );
});