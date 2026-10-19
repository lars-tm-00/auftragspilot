/* Cookielose Reichweitenmessung für Auftragspilot.
   Kein Cookie, keine Speicherung im Browser, keine Nutzer-ID, keine IP-Speicherung.
   Gesendet werden nur: Ereignisname, Seitenpfad, Sprache, Referrer-Domain, Gerätegruppe. */
(function () {
  var ENDPOINT = "https://n8n.larsomatic.org/webhook/ap-analytics";
  var host = location.hostname;
  var live = host === "larsomatic.org" || host === "www.larsomatic.org";
  if (!live) { window.apTrack = function () {}; return; }
  if (navigator.doNotTrack === "1" || window.doNotTrack === "1") { window.apTrack = function () {}; return; }

  var device = window.innerWidth <= 860 ? "mobile" : "desktop";
  var lang = document.documentElement.lang || "";
  var ref = "";
  try { ref = document.referrer ? new URL(document.referrer).hostname : ""; } catch (e) {}
  if (ref === host) ref = "";

  function track(e, x) {
    try {
      fetch(ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ e: e, p: location.pathname, l: lang, r: ref, d: device, x: x || "" }),
        keepalive: true,
      }).catch(function () {});
    } catch (err) {}
  }
  window.apTrack = track;
  track("pageview");

  // Abschnitte, die zum ersten Mal sichtbar werden
  if ("IntersectionObserver" in window) {
    var seen = {};
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting && !seen[en.target.id]) { seen[en.target.id] = 1; track("section_view", en.target.id); }
      });
    }, { threshold: 0.3 });
    ["video", "zahlen", "loesung", "branchen", "faq", "termin", "kontakt"].forEach(function (id) {
      var el = document.getElementById(id); if (el) io.observe(el);
    });
  }

  // Video
  var v = document.querySelector(".video-frame video");
  if (v) {
    var played = false, half = false;
    v.addEventListener("play", function () { if (!played) { played = true; track("video_play"); } });
    v.addEventListener("timeupdate", function () { if (!half && v.duration && v.currentTime / v.duration >= 0.5) { half = true; track("video_50"); } });
    v.addEventListener("ended", function () { track("video_end"); });
  }

  // Klicks auf Buttons und Links
  document.addEventListener("click", function (ev) {
    var a = ev.target.closest && ev.target.closest("a");
    if (!a) return;
    var h = a.getAttribute("href") || "", x = "";
    if (h === "#termin" || h.indexOf("cal.com") > -1) x = "demo";
    else if (h.indexOf("wa.me") > -1) x = "whatsapp";
    else if (h.indexOf("verlust-check") > -1) x = "verlust-check";
    else if (h.indexOf("mailto:") === 0) x = "mail";
    else return;
    var sec = a.closest("section[id]");
    track("cta_click", x + (sec ? ":" + sec.id : ""));
  });

  // FAQ
  document.querySelectorAll(".faq details").forEach(function (d, i) {
    d.addEventListener("toggle", function () { if (d.open) track("faq_open", String(i + 1)); });
  });

  // Verlust-Check
  var lf = document.getElementById("leakForm");
  if (lf) {
    var started = false;
    lf.addEventListener("input", function () { if (!started) { started = true; track("vc_start"); } });
    var res = document.getElementById("result");
    if (res && "MutationObserver" in window) {
      var done = false;
      new MutationObserver(function () {
        if (!done && res.classList.contains("is-visible")) {
          done = true;
          var sp = document.getElementById("speed");
          track("vc_result", sp ? sp.value : "");
        }
      }).observe(res, { attributes: true, attributeFilter: ["class"] });
    }
  }
})();
