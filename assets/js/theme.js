const THEME = "theme";
const DARK = "dark";
const LIGHT = "light";
const DARK_HIGHLIGHT = "#444";
const LIGHT_HIGHLIGHT = "#eee";
const GISCUS_LIGHT = "https://giscus.app/themes/light.css";
const GISCUS_DARK = "https://giscus.app/themes/dark.css";

// theme functions
const isDark = () => localStorage.getItem(THEME) === DARK

const saveTheme = (theme) => {
  localStorage.setItem(THEME, theme);
  setTheme();
};

const setGiscusTheme = () => {
  const iframe = document.getElementsByClassName("giscus-frame")[0];

  if (iframe) {
    iframe.contentWindow.postMessage(
      {
        giscus: {
          setConfig: {
            theme: `${isDark() ? GISCUS_DARK : GISCUS_LIGHT}`,
          },
        },
      },
      "https://giscus.app"
    );
  }
};

const setAudioPlayerTheme = () => {
  if(BeyondWords.Player.instances()[0]){
    BeyondWords.Player.instances()[0].highlightColor = isDark() ? DARK_HIGHLIGHT : LIGHT_HIGHLIGHT; 
  }
}

const setTheme = () => {
  const themeToggleIcon = document.getElementById("theme-toggle-icon");

  if (isDark()) {
    document.documentElement.classList.add(DARK);
    themeToggleIcon.style.transform = "rotate(180deg)";
  } else {
    document.documentElement.classList.remove(DARK);
    themeToggleIcon.style.transform = "rotate(0deg)";
  }

  setGiscusTheme();
  setAudioPlayerTheme();
};

document.addEventListener("keydown", function (e) {
  if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.keyCode === 76) {
    saveTheme(isDark() ? LIGHT : DARK);
  }
});

const sticky = navbar.offsetTop;

const setStickyness = () => {
  const navbar = document.getElementById("navbar");
  const banner = document.getElementsByClassName("banner")[0];

  if (window.pageYOffset >= sticky) {
    navbar.classList.add("fixed");
    banner.classList.add("mt-16");
  } else {
    navbar.classList.remove("fixed");
    banner.classList.remove("mt-16");
  }
};

const toggleNav = () => {
  const menuButton = document.getElementById("menu-btn");
  const mobileNav = document.getElementById("mobile-nav");

  if (menuButton.classList.contains("open")) {
    // nav should close
    menuButton.classList.remove("open");
    mobileNav.classList.add("hidden");
  } else {
    // nav should open
    menuButton.classList.add("open");
    mobileNav.classList.remove("hidden");
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
  if (e.key.toLowerCase() === "K".toLowerCase() && (e.ctrlKey || e.metaKey)) {
    e.preventDefault();
    showSearch();
  }

  // escape key
  if (e.key.toLowerCase() === "Escape".toLowerCase()) {
    hideSearch();
  }
});

if ("serviceWorker" in navigator) {
  navigator.serviceWorker.register("/service-worker.js");
}
