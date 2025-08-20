// chatbot-service/backend/static/script.js


async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();
  if (!message) return;

  appendMessage("You", message);
  input.value = "";

  try {
    const res = await fetch("/chatbot", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message })
    });

    const data = await res.json();
    appendMessage("Bot", data.response);
  } catch (error) {
    appendMessage("Bot", "Something went wrong!");
  }
}

function appendMessage(sender, text) {
  const chatBox = document.getElementById("chat-box");
  const msgDiv = document.createElement("div");
  msgDiv.innerHTML = `<strong>${sender}:</strong> ${text}`;
  chatBox.appendChild(msgDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}
