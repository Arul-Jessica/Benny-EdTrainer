// static/script.js
const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

sendBtn.addEventListener('click', () => {
    const question = userInput.value.trim();
    if (!question) return;
  
    // Display user's message
    chatBox.innerHTML += `<p><strong>You:</strong> ${question}</p>`;
    userInput.value = '';
  
    // Send question to backend
    fetch('/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question }),
    })
      .then(response => response.json())
      .then(data => {
        // Display Benny's response
        chatBox.innerHTML += `<p><strong>Benny:</strong> ${data.answer}</p>`;
        chatBox.scrollTop = chatBox.scrollHeight;
      });
  });