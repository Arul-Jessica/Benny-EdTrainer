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

  // Simulate sending the question to the backend
  chatBox.innerHTML += `<p><strong>Benny:</strong> I'm still learning! Can you clarify?</p>`;
  chatBox.scrollTop = chatBox.scrollHeight;
});