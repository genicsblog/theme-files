window.onscroll = () => {
  setStickyness();
};

const navbar = document.getElementById("navbar");
const banner = document.getElementById("banner");
const sticky = navbar.offsetTop;

const themeToggleIcon = document.getElementById("theme-toggle-icon");

if (localStorage.getItem("rotated") === "true") {
  themeToggleIcon.style.transform = "rotate(180deg)";
} else {
  themeToggleIcon.style.transform = "rotate(0deg)";
}

const setStickyness = () => {
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
    noResultsText: "<span class='mt-2 flex'>No results found</span>",
    searchResultTemplate: `<a class="search-item underline-none hover:border-{category}" href="{url}"><span>{title}</span></a>`,
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
  if (e.keyCode === 75 && (e.ctrlKey || e.metaKey)) {
    showSearch();
  }

  if (e.keyCode === 27) {
    hideSearch();
  }
});

const toggleTheme = () => {
  if (localStorage.getItem("color-theme")) {
    if (localStorage.getItem("color-theme") === "light") {
      document.documentElement.classList.add("dark");
      localStorage.setItem("color-theme", "dark");
    } else {
      document.documentElement.classList.remove("dark");
      localStorage.setItem("color-theme", "light");
    }
  } else {
    // if NOT set via local storage previously
    if (document.documentElement.classList.contains("dark")) {
      document.documentElement.classList.remove("dark");
      localStorage.setItem("color-theme", "light");
    } else {
      document.documentElement.classList.add("dark");
      localStorage.setItem("color-theme", "dark");
    }
  }

  if (localStorage.getItem("rotated") === "true") {
    themeToggleIcon.style.transform = "rotate(0deg)";
    localStorage.setItem("rotated", "false");
  } else {
    themeToggleIcon.style.transform = "rotate(180deg)";
    localStorage.setItem("rotated", "true");
  }
};

document
  .getElementById("search-container")
  .addEventListener("click", (event) => {
    if (event.target.id === "search-container") {
      hideSearch();
    }
  });
