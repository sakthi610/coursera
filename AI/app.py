from flask import Flask, render_template, request, jsonify
import google.generativeai as ai

app = Flask(__name__)

# API key and model setup
API_KEY = 'AIzaSyCA1fPpo59Z7X3k6hWymhIJP75r0QnNkJM'
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat()
history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_response():
    user_msg = request.json['message']
    history.append(f"User: {user_msg}")
    response = chat.send_message('\n'.join(history))
    history.append(f"Chatbot: {response.text}")
    return jsonify({'reply': response.text})

if __name__ == '__main__':
    app.run(debug=True)
