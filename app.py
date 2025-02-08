from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '').lower()
    answer = "I'm still learning! Can you clarify?"
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)