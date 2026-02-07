// ---------- THEME TOGGLE ----------
const toggle = document.getElementById("themeToggle");

if (toggle) {
  toggle.addEventListener("click", () => {
    const isDark =
      document.documentElement.getAttribute("data-theme") === "dark";

    if (isDark) {
      document.documentElement.removeAttribute("data-theme");
      toggle.textContent = "🌙";
    } else {
      document.documentElement.setAttribute("data-theme", "dark");
      toggle.textContent = "✨";
    }
  });
}


// ---------- DOCUMENT GENERATION ----------
async function generateDoc() {
  const text = document.getElementById("inputText").value;
  const output = document.getElementById("output");

  if (!text.trim()) {
    output.textContent = "Please paste some text.";
    return;
  }

  output.textContent = "⏳ Generating documentation...";

  try {
    const response = await fetch("https://genai-for-genz.onrender.com/generate", {

      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    });

    const data = await response.json();

    if (data.error) {
      output.textContent = "❌ " + data.error;
    } else {
      output.textContent = data.result;
    }
  } catch (err) {
    output.textContent = "⚠️ Server error. Try again.";
  }
}
