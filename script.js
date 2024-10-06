function appendMessage(text, sender) {
    const chatbox = document.getElementById('chatbox');
    const message = document.createElement('div');
    message.className = `message ${sender}`;
    message.innerText = text;
    chatbox.appendChild(message);
    chatbox.scrollTop = chatbox.scrollHeight; // Scroll to the bottom
}

function sendMessage() {
    const userInput = document.getElementById('user-input');
    const question = userInput.value;

    if (!question) return;

    appendMessage(question, 'user');
    userInput.value = '';

    // Check how many student inputs are already stored
    fetch('/query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question: question })
    })
    .then(response => response.json())
    .then(data => {
        appendMessage(data.response, 'bot');
    })
    .catch(error => {
        appendMessage("Error: " + error, 'bot');
    });
}
