---
---

const THEME = "theme";
const DARK = "dark";
const LIGHT = "light";

// dark mode functions
const isSomeThemeSaved = () => {
  return localStorage.getItem(THEME) !== null && localStorage.getItem(THEME) !== undefined;
}

const isDark = () => {
  return localStorage.getItem(THEME) === DARK ||
          (
            !isSomeThemeSaved() &&
            window.matchMedia &&
            window.matchMedia("(prefers-color-scheme: dark)").matches
          );
};

const saveTheme = (theme) => {
  localStorage.setItem(THEME, theme);
  setTheme();
};

const setTheme = () => {
  const themeToggleIcon = document.getElementById("theme-toggle-icon");

  if (isDark()) {
    document.documentElement.classList.add(DARK);
    themeToggleIcon.style.transform = "rotate(180deg)";
  } else {
    document.documentElement.classList.remove(DARK);
    themeToggleIcon.style.transform = "rotate(0deg)";
  }
};

document.addEventListener("keydown", function (e) {
  if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.keyCode === 76) {
    saveTheme(isDark() ? LIGHT : DARK);
  }
});

const sticky = navbar.offsetTop;

const setStickyness = () => {
  const navbar = document.getElementById("navbar");
  const banner = document.getElementById("banner");

  if (window.pageYOffset >= sticky) {
    navbar.classList.add("fixed");
    banner.classList.add("mt-16");
  } else {
    navbar.classList.remove("fixed");
    banner.classList.remove("mt-16");
  }
};

const toggleNav = () => {
  const menuOpen = document.getElementById("menu-open");
  const menuClose = document.getElementById("menu-close");
  const mobileNav = document.getElementById("mobile-nav");

  if (menuClose.classList.contains("hidden")) {
    // nav is opened
    menuOpen.classList.add("hidden");
    menuClose.classList.remove("hidden");
    mobileNav.classList.remove("hidden");
  } else {
    // nav is closed
    menuOpen.classList.remove("hidden");
    menuClose.classList.add("hidden");
    mobileNav.classList.add("hidden");
  }
};

const showSearch = () => {
  document.getElementById("search-container").classList.remove("hidden");
  document.getElementById("search-input").focus();
  const sjs = SimpleJekyllSearch({
    searchInput: document.getElementById("search-input"),
    resultsContainer: document.getElementById("results-container"),
    json: "/search.json",
    debounceTime: 500,
    noResultsText: `<span class="mt-4 flex">No results found</span>`,
    searchResultTemplate: `<a class="search-item underline-none hover:border-{category}" href="{{ site.baseurl }}{url}"><span>{title}</span></a>`,
  });
};

const hideSearch = () => {
  document.getElementById("search-container").classList.add("hidden");
  document.getElementById("search-input").value = "";
  document.getElementById("results-container").innerHTML = "";
};

// Detect keypress
// CMD + K -> Open search
// CTRL + K -> Open search
// ESC -> Hide search
document.addEventListener("keydown", function (e) {
  if ((e.key.toLowerCase() === "K".toLowerCase()) && (e.ctrlKey || e.metaKey)) {
    e.preventDefault();
    showSearch();
  }

  // escape key
  if ((e.key.toLowerCase() === "Escape".toLowerCase())) {
    hideSearch();
  }
});