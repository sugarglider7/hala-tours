/* Hala Tours Agadir — menu, desk hours, day picks, length filter, thumb index, dock, WhatsApp planner. */
(function () {
  "use strict";
  var d = document, root = d.documentElement;
  root.classList.add("js");
  var dataEl = d.getElementById("hala-data");
  var D = dataEl ? JSON.parse(dataEl.textContent) : null;
  var $ = function (s, c) { return (c || d).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || d).querySelectorAll(s)); };
  var fmt = function (s, o) { return s.replace(/\{(\w+)\}/g, function (_, k) { return o[k]; }); };

  /* ---------- menu sheet */
  var sheet = d.getElementById("sheet"), openers = $$('[aria-controls="sheet"]'), lastFocus = null;
  function setSheet(open) {
    if (!sheet) return;
    sheet.hidden = !open;
    openers.forEach(function (b) { b.setAttribute("aria-expanded", String(open)); });
    root.style.overflow = open ? "hidden" : "";
    if (open) { lastFocus = d.activeElement; var f = $("a,button", sheet); f && f.focus(); }
    else if (lastFocus) lastFocus.focus();
  }
  openers.forEach(function (b) { b.addEventListener("click", function () { setSheet(sheet.hidden); }); });
  if (sheet) {
    $(".sheet__close", sheet).addEventListener("click", function () { setSheet(false); });
    sheet.addEventListener("click", function (ev) {
      if (ev.target === sheet || ev.target.closest("a")) setSheet(false);
    });
    d.addEventListener("keydown", function (ev) {
      if (sheet.hidden) return;
      if (ev.key === "Escape") setSheet(false);
      if (ev.key === "Tab") { // keep focus inside the dialog
        var f = $$("a,button", sheet), first = f[0], last = f[f.length - 1];
        if (ev.shiftKey && d.activeElement === first) { ev.preventDefault(); last.focus(); }
        else if (!ev.shiftKey && d.activeElement === last) { ev.preventDefault(); first.focus(); }
      }
    });
  }
  if (!D) return;

  /* ---------- desk open / closed (Agadir time) */
  function deskStatus() {
    try {
      var parts = new Intl.DateTimeFormat("en-GB", { timeZone: D.tz, weekday: "short", hour: "2-digit", minute: "2-digit", hour12: false }).formatToParts(new Date());
      var p = {}; parts.forEach(function (x) { p[x.type] = x.value; });
      var day = p.weekday.slice(0, 2), now = p.hour.replace("24", "00") + ":" + p.minute;
      var row = D.hours.filter(function (h) { return h[0] === day; })[0];
      var open = row && now >= row[1] && now < row[2];
      var txt, next = row;
      if (open) txt = fmt(D.ui.open_now, { close: row[2] });
      else {
        if (row && now >= row[2]) { var i = D.hours.indexOf(row); next = D.hours[(i + 1) % 7]; }
        txt = fmt(D.ui.closed_now, { open: next[1] });
      }
      $$("[data-status]").forEach(function (a) { a.classList.toggle("is-open", open); $("[data-status-text]", a).textContent = txt; });
      $$("[data-status-badge]").forEach(function (b) { b.textContent = txt; b.hidden = false; b.classList.toggle("is-open", open); });
    } catch (e) { /* keep the static address */ }
  }
  deskStatus(); setInterval(deskStatus, 60000);

  /* ---------- picks (shared with the planner; kept for the session) */
  var KEY = "hala-picks", picks = [];
  try { picks = JSON.parse(sessionStorage.getItem(KEY) || "[]").filter(function (id) { return D.products[id]; }); } catch (e) {}
  var dockLabel = $("[data-dock-label]"), dockCount = $("[data-count]"), pickedList = $("[data-picked]"), pickedEmpty = $("[data-picked-empty]");
  function moodOf(id) { var row = d.getElementById("day-" + id), ch = row && row.closest(".ch"); return ch ? ch.className.match(/ch--(\w+)/)[1] : "cobalt"; }
  function renderPicks() {
    try { sessionStorage.setItem(KEY, JSON.stringify(picks)); } catch (e) {}
    $$("[data-pick]").forEach(function (b) { b.setAttribute("aria-pressed", String(picks.indexOf(b.dataset.pick) > -1)); });
    if (dockCount) {
      dockCount.hidden = !picks.length; dockCount.textContent = picks.length;
      dockLabel.textContent = picks.length ? D.ui.sticky_go : D.ui.sticky_idle;
    }
    if (pickedList) {
      pickedList.innerHTML = "";
      picks.forEach(function (id) {
        var li = d.createElement("li"); li.className = "c-" + moodOf(id);
        li.appendChild(d.createTextNode(D.products[id]));
        var x = d.createElement("button"); x.type = "button"; x.setAttribute("aria-label", D.s.remove + ": " + D.products[id]);
        x.innerHTML = '<svg class="ico" aria-hidden="true"><use href="#i-close"/></svg>';
        x.addEventListener("click", function () { picks.splice(picks.indexOf(id), 1); renderPicks(); });
        li.appendChild(x); pickedList.appendChild(li);
      });
      pickedEmpty.hidden = !!picks.length;
    }
  }
  $$("[data-pick]").forEach(function (b) {
    b.addEventListener("click", function () {
      var id = b.dataset.pick, i = picks.indexOf(id);
      if (i > -1) picks.splice(i, 1); else picks.push(id);
      renderPicks();
    });
  });
  renderPicks();

  /* ---------- length filter */
  var chips = $$(".chip[data-len]");
  chips.forEach(function (c) {
    c.addEventListener("click", function () {
      var len = c.dataset.len;
      chips.forEach(function (x) { x.setAttribute("aria-pressed", String(x === c)); });
      $$(".ch").forEach(function (ch) {
        var shown = 0;
        $$(".day", ch).forEach(function (row) {
          var ok = !len || row.dataset.lengths.split(" ").indexOf(len) > -1;
          row.classList.toggle("is-out", !ok); if (ok) shown++;
        });
        ch.classList.toggle("is-empty", !shown);
        $(".ch__none", ch).hidden = !!shown;
      });
      var r = $(".lenbar").getBoundingClientRect();
      if (r.top < 0) $(".lenbar").scrollIntoView({ block: "start" });
    });
  });

  /* ---------- observers: reveal, thumb index, dock */
  if ("IntersectionObserver" in window) {
    var reveal = new IntersectionObserver(function (es) {
      es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("is-in"); reveal.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -10% 0px" });
    $$(".ch,.rv").forEach(function (el) { reveal.observe(el); });

    var guide = $("#guide");
    if (guide) new IntersectionObserver(function (es) { d.body.classList.toggle("guide-on", es[0].isIntersecting); }, { rootMargin: "-50% 0px -50% 0px" }).observe(guide);
    var thumbs = {};
    $$("[data-thumb]").forEach(function (t) { thumbs[t.dataset.thumb] = t; });
    var chObs = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (en.isIntersecting) {
          Object.keys(thumbs).forEach(function (k) { thumbs[k].classList.toggle("is-on", k === en.target.dataset.mood); });
        }
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    $$(".ch").forEach(function (ch) { chObs.observe(ch); });

    var dock = $("[data-dock]"), hideFor = new Set();
    if (dock) {
      var dObs = new IntersectionObserver(function (es) {
        es.forEach(function (en) { if (en.isIntersecting) hideFor.add(en.target); else hideFor.delete(en.target); });
        dock.classList.toggle("is-hidden", hideFor.size > 0);
      });
      ["#plan", "#foot"].forEach(function (s) { var el = $(s); el && dObs.observe(el); });
    }
  }

  /* ---------- planner → WhatsApp */
  var form = d.getElementById("planner");
  if (!form) return;
  var S = D.s, kids = form.elements.kids, agesBox = $("[data-ages]", form), ok = $("[data-ok]", form);
  var dateIn = form.elements.date, today = new Date();
  var iso = function (x) { return x.getFullYear() + "-" + String(x.getMonth() + 1).padStart(2, "0") + "-" + String(x.getDate()).padStart(2, "0"); };
  dateIn.min = iso(today);
  kids.addEventListener("input", function () { agesBox.hidden = !(parseInt(kids.value, 10) > 0); });

  function showErr(name, on, field) {
    var el = $('[data-err="' + name + '"]', form); if (el) el.hidden = !on;
    if (field) { field.setAttribute("aria-invalid", String(on)); if (on) field.setAttribute("aria-describedby", (field.id || name) + "-err"); }
    if (el && field) el.id = (field.id || name) + "-err";
  }
  function compose() {
    var f = form.elements, L = [S.wa_intro, ""];
    var moods = $$('input[name="mood"]:checked', form).map(function (x) { return D.moods[x.value]; });
    if (moods.length) L.push("• " + S.wa_moods + ": " + moods.join(", "));
    if (picks.length) L.push("• " + S.wa_picked + ": " + picks.map(function (id) { return D.products[id]; }).join("; "));
    var len = ($('input[name="length"]:checked', form) || {}).value;
    if (len) L.push("• " + S.wa_length + ": " + D.lengths[len]);
    if (f.date.value) {
      var dt = new Date(f.date.value + "T12:00:00");
      L.push("• " + S.wa_date + ": " + dt.toLocaleDateString(D.lang === "fr" ? "fr-FR" : "en-GB", { weekday: "short", day: "numeric", month: "short", year: "numeric" }));
    }
    var a = parseInt(f.adults.value, 10) || 0, k = parseInt(f.kids.value, 10) || 0;
    var ppl = a === 1 ? S.wa_adult : fmt(S.wa_adults, { n: a });
    if (k > 0) ppl += ", " + (k === 1 ? S.wa_kid : fmt(S.wa_kids, { n: k })) + (f.ages.value.trim() ? " (" + S.wa_ages + ": " + f.ages.value.trim() + ")" : "");
    L.push("• " + S.wa_people + ": " + ppl);
    if (f.stay.value.trim()) L.push("• " + S.wa_stay + ": " + f.stay.value.trim());
    if (f.name.value.trim()) L.push("• " + S.wa_name + ": " + f.name.value.trim());
    if (f.msg.value.trim()) L.push("• " + S.wa_msg + ": " + f.msg.value.trim());
    L.push("", S.wa_outro);
    return L.join("\n");
  }
  form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    var f = form.elements, bad = null;
    var hasWhat = $$('input[name="mood"]:checked', form).length || picks.length || f.msg.value.trim();
    showErr("what", !hasWhat); if (!hasWhat) bad = bad || $('input[name="mood"]', form);
    var a = parseInt(f.adults.value, 10);
    var aBad = !(a >= 1 && a <= 60); showErr("adults", aBad, f.adults); if (aBad) bad = bad || f.adults;
    var dBad = !!f.date.value && f.date.value < iso(new Date()); showErr("date", dBad, f.date); if (dBad) bad = bad || f.date;
    if (bad) { bad.focus(); return; }
    var text = compose(), href = D.wa + "?text=" + encodeURIComponent(text);
    $("[data-retry]", form).href = href;
    $("[data-mail]", form).href = "mailto:" + D.email + "?subject=" + encodeURIComponent(S.mail_subject) + "&body=" + encodeURIComponent(text);
    ok.hidden = false; ok.focus();
    window.open(href, "_blank", "noopener");
  });
})();
