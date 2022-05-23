// control variable to prevent changing langName's text from "Copy" to language name
// if the user clicks on the "Copy" button. It should wait for the setTimeout to finish
let shouldToggleName = true;

function extractLanguage(classes) {
  const match = classes.match(/language-(\w+)/);
  return match ? match[1] : null;
}

// Custom code to add language info to codeblocks
setTimeout(() => {
  const codeBlocks = document.querySelectorAll("pre");

  codeBlocks.forEach((block) => {
      var langNameHolder = document.createElement("div");
      langNameHolder.style.position = "relative";

      const langName = document.createElement("button");
      langName.classList.add("lang-name");
      langName.textContent = extractLanguage(block.className);
      langName.addEventListener("click", (e) => {
          e.preventDefault();
          shouldToggleName = false;

          const code = block.querySelector("code").innerText;
          navigator.clipboard.writeText(code);

          langName.textContent = "Copied!";

          setTimeout(() => {
              langName.textContent = "Copy";
              shouldToggleName = true;
          }, 1500);
      });

      langNameHolder.appendChild(langName);
      block.parentElement.prepend(langNameHolder);

      block.addEventListener("mouseenter", (e) => {
          if(shouldToggleName) langName.textContent = "Copy";
      });

      langNameHolder.addEventListener("mouseenter", (e) => {
        if(shouldToggleName) langName.textContent = "Copy";
      });

      block.addEventListener("mouseleave", () => {
          if(shouldToggleName) langName.textContent = extractLanguage(block.className);
      });
  })
}, 500);