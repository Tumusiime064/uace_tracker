self.addEventListener("install", (e) => {
  console.log("UACE Tracker Service Worker Installed");
});
self.addEventListener("fetch", (e) => {
  // Directly fetches live content from your Render server
});
