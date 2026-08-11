// ==========================================================================
// Anchorline — main.js
// Handles: mobile nav toggle, FAQ accordion, contact form validation,
// footer year.
// ==========================================================================

(function () {
  "use strict";

  /* -------------------- Dark / light mode -------------------- */
  var themeToggle = document.getElementById("themeToggle");
  var root = document.documentElement;
  var STORAGE_KEY = "laiba-theme";

  function applyTheme(theme) {
    if (theme === "dark") {
      root.setAttribute("data-theme", "dark");
      themeToggle.setAttribute("aria-pressed", "true");
      themeToggle.setAttribute("aria-label", "Switch to light mode");
    } else {
      root.removeAttribute("data-theme");
      themeToggle.setAttribute("aria-pressed", "false");
      themeToggle.setAttribute("aria-label", "Switch to dark mode");
    }
  }

  if (themeToggle) {
    var saved = null;
    try { saved = localStorage.getItem(STORAGE_KEY); } catch (err) { /* storage unavailable */ }

    var prefersDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
    applyTheme(saved || (prefersDark ? "dark" : "light"));

    themeToggle.addEventListener("click", function () {
      var isDark = root.getAttribute("data-theme") === "dark";
      var next = isDark ? "light" : "dark";
      applyTheme(next);
      try { localStorage.setItem(STORAGE_KEY, next); } catch (err) { /* storage unavailable */ }
    });
  }

  /* -------------------- Mobile navigation -------------------- */
  var navToggle = document.getElementById("navToggle");
  var primaryNav = document.getElementById("primaryNav");

  if (navToggle && primaryNav) {
    navToggle.addEventListener("click", function () {
      var isOpen = navToggle.getAttribute("aria-expanded") === "true";
      navToggle.setAttribute("aria-expanded", String(!isOpen));
      primaryNav.classList.toggle("is-open", !isOpen);
    });

    // Close menu after choosing a link (mobile)
    primaryNav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        navToggle.setAttribute("aria-expanded", "false");
        primaryNav.classList.remove("is-open");
      });
    });

    // Close on Escape
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && primaryNav.classList.contains("is-open")) {
        navToggle.setAttribute("aria-expanded", "false");
        primaryNav.classList.remove("is-open");
        navToggle.focus();
      }
    });
  }

  /* -------------------- FAQ accordion -------------------- */
  var triggers = document.querySelectorAll(".accordion-trigger");

  triggers.forEach(function (trigger) {
    trigger.addEventListener("click", function () {
      var expanded = trigger.getAttribute("aria-expanded") === "true";
      var panel = document.getElementById(trigger.getAttribute("aria-controls"));

      // Close all other panels (single-open accordion)
      triggers.forEach(function (t) {
        if (t !== trigger) {
          t.setAttribute("aria-expanded", "false");
          var p = document.getElementById(t.getAttribute("aria-controls"));
          if (p) p.hidden = true;
        }
      });

      trigger.setAttribute("aria-expanded", String(!expanded));
      if (panel) panel.hidden = expanded;
    });
  });

  /* -------------------- Contact form -------------------- */
  var form = document.getElementById("contactForm");
  var status = document.getElementById("formStatus");

  function setFieldError(fieldId, message) {
    var field = document.getElementById(fieldId);
    var errorEl = document.getElementById(fieldId + "-error");
    var row = field ? field.closest(".form-row") : null;

    if (errorEl) errorEl.textContent = message || "";
    if (row) row.classList.toggle("has-error", Boolean(message));
  }

  function isValidEmail(value) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
  }

  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();

      var name = document.getElementById("name");
      var email = document.getElementById("email");
      var projectType = document.getElementById("projectType");
      var message = document.getElementById("message");

      var valid = true;

      if (!name.value.trim()) {
        setFieldError("name", "Please enter your name.");
        valid = false;
      } else {
        setFieldError("name", "");
      }

      if (!email.value.trim()) {
        setFieldError("email", "Please enter your email address.");
        valid = false;
      } else if (!isValidEmail(email.value.trim())) {
        setFieldError("email", "Please enter a valid email address.");
        valid = false;
      } else {
        setFieldError("email", "");
      }

      if (!projectType.value) {
        setFieldError("projectType", "Please select a project type.");
        valid = false;
      } else {
        setFieldError("projectType", "");
      }

      if (!message.value.trim()) {
        setFieldError("message", "Please add a few details about your project.");
        valid = false;
      } else {
        setFieldError("message", "");
      }

      if (!valid) {
        status.textContent = "Please fix the highlighted fields and try again.";
        status.className = "form-status error";
        return;
      }

      // NOTE: This form has no backend connected. Replace this block with a
      // real submission — e.g. POST to your own API endpoint, or a form
      // service such as Formspree — before publishing this site.
      status.textContent = "Thanks — your message has been prepared. Connect a form backend to actually send it.";
      status.className = "form-status success";
      form.reset();
    });
  }

  /* -------------------- Footer year -------------------- */
  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

})();
