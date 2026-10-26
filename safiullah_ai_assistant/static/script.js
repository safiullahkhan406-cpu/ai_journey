const form = document.getElementById("chatForm");
const input = document.getElementById("message");
const chat = document.getElementById("chat");
const statusText = document.getElementById("status");
const sendButton = document.getElementById("sendButton");
const newChatButton = document.getElementById("newChatButton");

// Message ko safely website par dikhayein
function addMessage(sender, message, className) {
    const box = document.createElement("div");
    box.className = "message " + className;

    const label = document.createElement("strong");
    label.textContent = sender + ": ";

    const text = document.createElement("span");
    text.textContent = message;

    box.appendChild(label);
    box.appendChild(text);
    chat.appendChild(box);

    chat.scrollTop = chat.scrollHeight;
}

// User ka sawal AI ko bhejein
form.addEventListener("submit", async function(event) {
    event.preventDefault();

    const message = input.value.trim();

    if (!message) return;

    addMessage("You", message, "user");
    input.value = "";
    sendButton.disabled = true;
    statusText.textContent = "AI jawab tayyar kar raha hai...";

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.answer || "Request failed.");
        }

        addMessage("AI", data.answer, "assistant");
        statusText.textContent = "";

    } catch (error) {
        addMessage(
            "Error",
            error.message || "Connection problem. Dobara koshish karein.",
            "assistant"
        );

        statusText.textContent = "Jawab hasil nahi ho saka.";

    } finally {
        sendButton.disabled = false;
        input.focus();
    }
});

// Nayi conversation shuru karein
newChatButton.addEventListener("click", async function() {
    newChatButton.disabled = true;

    try {
        const response = await fetch("/new-chat", {
            method: "POST"
        });

        if (!response.ok) {
            throw new Error("New chat start nahi ho saka.");
        }

        chat.replaceChildren();

        addMessage(
            "AI",
            "Assalam-o-Alaikum! Nayi conversation shuru ho gayi hai.",
            "assistant"
        );

        statusText.textContent = "";

    } catch (error) {
        statusText.textContent = error.message;

    } finally {
        newChatButton.disabled = false;
    }
});