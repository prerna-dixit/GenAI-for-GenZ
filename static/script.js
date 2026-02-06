async function generateDoc() {
  const text = document.getElementById("inputText").value;
  const output = document.getElementById("output");

  output.textContent = "⏳ Generating documentation...";

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
