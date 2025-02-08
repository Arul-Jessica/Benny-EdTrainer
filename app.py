from flask import Flask, render_template, request, jsonify
import wikipediaapi

# wiki_wiki = wikipediaapi.Wikipedia('en')


user_agent = "Benny-EdTrainer/1.0 (Contact: boraborasaturn@gmail.com)"  # Replace with your details
wiki_wiki = wikipediaapi.Wikipedia(user_agent=user_agent, language="en")


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '').lower()

    page = wiki_wiki.page(question)
    if page.exists():
        summary = page.summary[:500] + "..."  # Limit summary length
        answer = f"Here's what I found about '{question}': {summary}"
    else:
        answer = "I couldn't find any information on that topic. Can you clarify?"

    return jsonify({'answer': answer})
if __name__ == '__main__':
    app.run(debug=True)