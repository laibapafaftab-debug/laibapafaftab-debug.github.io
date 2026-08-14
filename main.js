
// Laiba.dev - main.js

(function () {
  "use strict";

  const root = document.documentElement;
  const themeToggle = document.getElementById("themeToggle");
  const STORAGE_KEY = "laiba-theme";

  // Theme
  function applyTheme(theme) {
    if (theme === "dark") {
      root.setAttribute("data-theme", "dark");
    } else {
      root.removeAttribute("data-theme");
    }
  }

  if (themeToggle) {
    let saved = localStorage.getItem(STORAGE_KEY);
    let systemDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

    applyTheme(saved || (systemDark ? "dark" : "light"));

    themeToggle.addEventListener("click", () => {
      let dark = root.getAttribute("data-theme") === "dark";
      let next = dark ? "light" : "dark";

      applyTheme(next);
      localStorage.setItem(STORAGE_KEY, next);
    });
  }


  // Mobile menu
  const navToggle = document.getElementById("navToggle");
  const nav = document.getElementById("primaryNav");

  if (navToggle && nav) {
    navToggle.onclick = () => {
      let open = navToggle.getAttribute("aria-expanded") === "true";

      navToggle.setAttribute("aria-expanded", !open);
      nav.classList.toggle("is-open");
    };
  }


  // Scroll Reveal
  const elements = document.querySelectorAll(
    "section, .service-card, .price-card, .project-card, .work-card, .cta-band"
  );

  elements.forEach(el => {
    el.classList.add("reveal-ready");
  });


  const observer = new IntersectionObserver(entries => {

    entries.forEach(entry => {

      if(entry.isIntersecting){
        entry.target.classList.add("is-visible");
      }

    });

  },{
    threshold:0.15
  });


  elements.forEach(el => observer.observe(el));


  // Scroll top button
  const scrollBtn = document.getElementById("scrollTopBtn");

  window.addEventListener("scroll",()=>{

    if(scrollBtn){
      if(window.scrollY > 400){
        scrollBtn.classList.add("visible");
      }
      else{
        scrollBtn.classList.remove("visible");
      }
    }

  });


  if(scrollBtn){

    scrollBtn.onclick=()=>{

      window.scrollTo({
        top:0,
        behavior:"smooth"
      });

    };

  }


  // Footer year
  const year = document.getElementById("year");

  if(year){
    year.textContent = new Date().getFullYear();
  }


})();
