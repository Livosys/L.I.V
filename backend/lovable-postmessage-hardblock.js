// HARD BLOCK postMessage warnings in Lovable preview
// Lägg denna fil i Lovable-projektet och importera den tidigt

(function () {
  const ALLOWED = window.location.origin;

  const original = window.postMessage;
  window.postMessage = function (message, targetOrigin, transfer) {
    if (
      targetOrigin === ALLOWED ||
      targetOrigin === "*" ||
      targetOrigin === undefined ||
      targetOrigin === null
    ) {
      return original.call(window, message, targetOrigin, transfer);
    }
    // BLOCKERA ALLT ANNAT (ingen console.error)
    return;
  };

  // Tysta console.error för postMessage
  const originalError = console.error;
  console.error = function (...args) {
    const msg = args.join(" ");
    if (msg.includes("postMessage") && msg.includes("DOMWindow")) {
      return;
    }
    originalError.apply(console, args);
  };
})();
