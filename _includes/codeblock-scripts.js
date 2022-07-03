// control variable to prevent changing langName's text from "Copy" to language name
// if the user clicks on the "Copy" button. It should wait for the setTimeout to finish
let shouldToggleName = true;

function extractLanguage(classes) {
  const match = classes.match(/language-(\w+)/);
  return match ? match[1] : null;
}

function initCodeBlocks() {
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
        if (!shouldToggleName) return;
        shouldToggleName = false;

        const code = block.querySelector("code").innerText;
        navigator.clipboard.writeText(code);

        langName.textContent = "Copied!";

        setTimeout(() => {
          shouldToggleName = true;
          let text = "";
          document.querySelectorAll(":hover").forEach((el) => {
            if (el.classList.contains("highlight")) {
              text = "Copy";
            } else {
              if (text === "") text = extractLanguage(block.className);
            }
          });
          langName.textContent = text;
        }, 1500);
      });

      langNameHolder.appendChild(langName);
      block.parentElement.prepend(langNameHolder);

      block.addEventListener("mouseenter", (e) => {
        if (shouldToggleName) langName.textContent = "Copy";
      });

      langNameHolder.addEventListener("mouseenter", (e) => {
        if (shouldToggleName) langName.textContent = "Copy";
      });

      block.addEventListener("mouseleave", () => {
        if (shouldToggleName)
          langName.textContent = extractLanguage(block.className);
      });
    });
  }, 500);
}
