/* Hala Tours Agadir — menu, desk hours, day picks, length filter, thumb index, dock, WhatsApp forms. */
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

  /* ---------- picks ("Add to my day"), kept across pages and visits */
  var KEY = "hala-picks", picks = [], store = null;
  try { store = window.localStorage; picks = JSON.parse(store.getItem(KEY) || "[]"); } catch (e) { store = null; }
  if (!Array.isArray(picks)) picks = [];
  picks = picks.filter(function (id, i) { return D.products[id] && picks.indexOf(id) === i; });
  var dockLink = $(".dock__plan"), dockLabel = $("[data-dock-label]"), dockCount = $("[data-count]");
  var pickedList = $("[data-picked]"), pickedEmpty = $("[data-picked-empty]");
  function renderPicks() {
    try { store && store.setItem(KEY, JSON.stringify(picks)); } catch (e) {}
    $$("[data-pick]").forEach(function (b) { b.setAttribute("aria-pressed", String(picks.indexOf(b.dataset.pick) > -1)); });
    if (dockCount && !dockLink.hasAttribute("data-static")) {
      dockCount.hidden = !picks.length; dockCount.textContent = picks.length;
      dockLabel.textContent = picks.length ? D.ui.sticky_go : D.ui.sticky_idle;
    }
    if (pickedList) {
      pickedList.innerHTML = "";
      picks.forEach(function (id) {
        var li = d.createElement("li"); li.className = "c-" + (D.pc[id] || "cobalt");
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
  window.addEventListener("storage", function (ev) {
    if (ev.key !== KEY) return;
    try { picks = JSON.parse(ev.newValue || "[]").filter(function (id) { return D.products[id]; }); } catch (e) { picks = []; }
    renderPicks();
  });
  renderPicks();

  /* ---------- length filter (works on every chapter on the page; on the homepage it also reveals hidden rows) */
  var chips = $$(".chip[data-len]"), bar = $(".lenbar");
  chips.forEach(function (c) {
    c.addEventListener("click", function () {
      var len = c.dataset.len;
      chips.forEach(function (x) { x.setAttribute("aria-pressed", String(x === c)); });
      $$(".ch").forEach(function (ch) {
        var shown = 0;
        ch.classList.toggle("is-filtered", !!len);
        $$(".day", ch).forEach(function (row) {
          var ok = !len || row.dataset.lengths.split(" ").indexOf(len) > -1;
          row.classList.toggle("is-out", !ok); if (ok) shown++;
        });
        ch.classList.toggle("is-empty", !shown);
        $(".ch__none", ch).hidden = !!shown;
      });
      if (bar && bar.getBoundingClientRect().top < 0) bar.scrollIntoView({ block: "start" });
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
        if (en.isIntersecting) Object.keys(thumbs).forEach(function (k) { thumbs[k].classList.toggle("is-on", k === en.target.dataset.mood); });
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    $$(".ch").forEach(function (ch) { chObs.observe(ch); });

    var dock = $("[data-dock]"), hideFor = new Set();
    if (dock) {
      var dObs = new IntersectionObserver(function (es) {
        es.forEach(function (en) { if (en.isIntersecting) hideFor.add(en.target); else hideFor.delete(en.target); });
        dock.classList.toggle("is-hidden", hideFor.size > 0);
      });
      $$("[data-dock-hide]").forEach(function (el) { dObs.observe(el); });
    }
  }

  /* ---------- WhatsApp forms: plan (planner), day (one day), transfer */
  var S = D.s;
  var iso = function (x) { return x.getFullYear() + "-" + String(x.getMonth() + 1).padStart(2, "0") + "-" + String(x.getDate()).padStart(2, "0"); };
  var nice = function (v) {
    var dt = new Date(v + "T12:00:00");
    return dt.toLocaleDateString(D.lang === "fr" ? "fr-FR" : "en-GB", { weekday: "short", day: "numeric", month: "short", year: "numeric" });
  };
  var val = function (form, name) { var el = form.elements[name]; return el ? String(el.value || "").trim() : ""; };
  var line = function (L, label, v) { if (v) L.push("• " + label + ": " + v); };
  var lineFr = function (L, label, v) { if (v) L.push("• " + label + (D.lang === "fr" ? " : " : ": ") + v); };
  var add = D.lang === "fr" ? lineFr : line;

  function people(form) {
    var a = parseInt(val(form, "adults"), 10) || 0, k = parseInt(val(form, "kids"), 10) || 0, ages = val(form, "ages");
    var txt = a === 1 ? S.wa_adult : fmt(S.wa_adults, { n: a });
    if (k > 0) txt += ", " + (k === 1 ? S.wa_kid : fmt(S.wa_kids, { n: k })) + (ages ? " (" + S.wa_ages + (D.lang === "fr" ? " : " : ": ") + ages + ")" : "");
    return txt;
  }
  var COMPOSE = {
    plan: function (form) {
      var L = [S.wa_intro, ""];
      var moods = $$('input[name="mood"]:checked', form).map(function (x) { return D.moods[x.value]; });
      add(L, S.wa_moods, moods.join(", "));
      add(L, S.wa_picked, picks.map(function (id) { return D.products[id]; }).join(D.lang === "fr" ? " ; " : "; "));
      var len = ($('input[name="length"]:checked', form) || {}).value;
      add(L, S.wa_length, len ? D.lengths[len] : "");
      add(L, S.wa_date, val(form, "date") && nice(val(form, "date")));
      add(L, S.wa_people, people(form));
      add(L, S.wa_stay, val(form, "stay"));
      add(L, S.wa_name, val(form, "name"));
      add(L, S.wa_msg, val(form, "msg"));
      L.push("", S.wa_outro);
      return L;
    },
    day: function (form) {
      var L = [fmt(S.d_intro, { day: D.products[form.dataset.day] }), ""];
      add(L, S.wa_date, val(form, "date") && nice(val(form, "date")));
      add(L, S.wa_people, people(form));
      add(L, S.wa_stay, val(form, "stay"));
      L.push("", S.d_outro);
      return L;
    },
    transfer: function (form) {
      var L = [S.t_intro, ""], r = form.elements.route;
      add(L, S.t_route, r.value ? r.options[r.selectedIndex].text : "");
      add(L, S.t_date, val(form, "date") && nice(val(form, "date")));
      add(L, S.t_time, val(form, "time"));
      add(L, S.t_flight, val(form, "flight"));
      add(L, S.t_people, val(form, "people"));
      add(L, S.t_bags, val(form, "bags"));
      add(L, S.t_stay, val(form, "stay"));
      add(L, S.t_name, val(form, "name"));
      L.push("", S.t_outro);
      return L;
    }
  };

  function showErr(form, name, on, field) {
    var el = $('[data-err="' + name + '"]', form);
    if (el) { el.hidden = !on; el.id = el.id || (form.dataset.wa + "-" + name + "-err"); }
    if (field) {
      field.setAttribute("aria-invalid", String(on));
      if (el) {
        var ids = (field.getAttribute("aria-describedby") || "").split(" ").filter(function (x) { return x && x !== el.id; });
        if (on) ids.push(el.id);
        if (ids.length) field.setAttribute("aria-describedby", ids.join(" ")); else field.removeAttribute("aria-describedby");
      }
    }
    return on;
  }
  function validate(form) {
    var kind = form.dataset.wa, f = form.elements, bad = [], today = iso(new Date());
    if (kind === "plan") {
      var hasWhat = $$('input[name="mood"]:checked', form).length || picks.length || val(form, "msg");
      if (showErr(form, "what", !hasWhat)) bad.push($('input[name="mood"]', form));
    }
    if (f.adults) { var a = parseInt(f.adults.value, 10); if (showErr(form, "adults", !(a >= 1 && a <= 60), f.adults)) bad.push(f.adults); }
    if (kind === "transfer") {
      if (showErr(form, "route", !f.route.value, f.route)) bad.push(f.route);
      if (showErr(form, "date", !f.date.value || f.date.value < today, f.date)) bad.push(f.date);
      var n = parseInt(f.people.value, 10); if (showErr(form, "people", !(n >= 1 && n <= 60), f.people)) bad.push(f.people);
    } else if (f.date) {
      if (showErr(form, "date", !!f.date.value && f.date.value < today, f.date)) bad.push(f.date);
    }
    return bad[0] || null;
  }

  $$("form[data-wa]").forEach(function (form) {
    var ok = $("[data-ok]", form), kids = form.elements.kids, agesBox = $("[data-ages]", form);
    if (form.elements.date) form.elements.date.min = iso(new Date());
    if (kids && agesBox) kids.addEventListener("input", function () { agesBox.hidden = !(parseInt(kids.value, 10) > 0); });
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var bad = validate(form);
      if (bad) { var det = bad.closest("details"); if (det) det.open = true; bad.focus(); return; }
      var text = COMPOSE[form.dataset.wa](form).join("\n"), href = D.wa + "?text=" + encodeURIComponent(text);
      $("[data-retry]", form).href = href;
      $("[data-mail]", form).href = "mailto:" + D.email + "?subject=" + encodeURIComponent(S.mail_subject) + "&body=" + encodeURIComponent(text);
      ok.hidden = false; ok.focus();
      window.open(href, "_blank", "noopener");
    });
  });
})();
