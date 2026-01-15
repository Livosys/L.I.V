// FIX: blockera postMessage-fel från fel origins i Lovable preview

(function () {
  const ALLOWED_ORIGIN = window.location.origin;

  const originalPostMessage = window.postMessage;
  window.postMessage = function (message, targetOrigin, transfer) {
    if (targetOrigin !== ALLOWED_ORIGIN && targetOrigin !== "*") {
      return;
    }
    return originalPostMessage.call(window, message, targetOrigin, transfer);
  };
})();
