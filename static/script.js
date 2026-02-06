async function generateDoc() {
  const text = document.getElementById("inputText").value;
  const output = document.getElementById("output");

  output.textContent = "⏳ Generating documentation...";

  const toggle = document.getElementById("themeToggle");

toggle.addEventListener("click", () => {
  const current = document.documentElement.getAttribute("data-theme");

  if (current === "dark") {
    document.documentElement.removeAttribute("data-theme");
    toggle.textContent = "☾";
  } else {
    document.documentElement.setAttribute("data-theme", "dark");
    toggle.textContent = "☀";
  }
});


  const response = await fetch("/generate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ text })
  });

  const data = await response.json();

  if (data.error) {
    output.textContent = "❌ " + data.error;
  } else {
    output.textContent = data.result;
  }
}
