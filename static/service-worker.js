self.addEventListener('install', e => {
  self.skipWaiting();
});

self.addEventListener('fetch', event => {
  // Simple network-first fallback cache for static resources
  event.respondWith(
    fetch(event.request).catch(() => caches.match(event.request))
  );
});
