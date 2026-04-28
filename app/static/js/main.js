
document.addEventListener('DOMContentLoaded', () => {
    const chatWindow = document.getElementById('chat-window');
    const chatForm = document.getElementById('chat-form');
    const messageInput = document.getElementById('message-input');
    const sendButton = chatForm.querySelector('button');

    let conversationId = null; 

    // Focus the input field on page load
    messageInput.focus();

    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const message = messageInput.value.trim();
        if (!message) return;

        appendMessage(message, 'user');
        messageInput.value = '';
        messageInput.disabled = true;
        sendButton.disabled = true;

        showTypingIndicator();
        scrollToBottom();

        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message, conversation_id: conversationId }),
            });

            removeTypingIndicator();

            if (!response.ok) {
                const errorData = await response.json().catch(() => null);
                const errorMessage = errorData?.error || 'Sorry, something went wrong.';
                appendMessage(errorMessage, 'bot', true);
                return;
            }

            const data = await response.json();
            conversationId = data.conversation_id;
            
            // Simulate real-time typing effect
            await appendMessageTyped(data.response, 'bot');

        } catch (error) {
            console.error('Fetch error:', error);
            removeTypingIndicator();
            appendMessage('Network error. Please check your connection.', 'bot', true);
        } finally {
            messageInput.disabled = false;
            sendButton.disabled = false;
            messageInput.focus();
            scrollToBottom();
        }
    });

    function appendMessage(content, sender, isError = false) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', `${sender}-message`);

        const contentDiv = document.createElement('div');
        contentDiv.classList.add('message-content');

        const p = document.createElement('p');
        p.textContent = content;
        
        if (isError) {
            p.style.color = 'hsl(350, 70%, 60%)';
        }

        contentDiv.appendChild(p);
        messageDiv.appendChild(contentDiv);
        chatWindow.appendChild(messageDiv);
        scrollToBottom();
    }

    async function appendMessageTyped(content, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', `${sender}-message`);

        const contentDiv = document.createElement('div');
        contentDiv.classList.add('message-content');

        const p = document.createElement('p');
        contentDiv.appendChild(p);
        messageDiv.appendChild(contentDiv);
        chatWindow.appendChild(messageDiv);
        
        const words = content.split(' ');
        for (let i = 0; i < words.length; i++) {
            p.textContent += words[i] + (i === words.length - 1 ? '' : ' ');
            scrollToBottom();
            await new Promise(resolve => setTimeout(resolve, 30 + Math.random() * 50));
        }
    }

    function showTypingIndicator() {
        const indicator = document.createElement('div');
        indicator.id = 'typing-indicator';
        indicator.classList.add('message', 'bot-message', 'typing-indicator');
        indicator.innerHTML = `<span></span><span></span><span></span>`;
        chatWindow.appendChild(indicator);
    }

    function removeTypingIndicator() {
        const indicator = document.getElementById('typing-indicator');
        if (indicator) {
            indicator.remove();
        }
    }

    function scrollToBottom() {
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }
});
