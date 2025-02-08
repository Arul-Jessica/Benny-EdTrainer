from flask import Flask, render_template, request, jsonify
import wikipediaapi
from transformers import pipeline
# wiki_wiki = wikipediaapi.Wikipedia('en')


user_agent = "Benny-EdTrainer/1.0 (Contact: boraborasaturn@gmail.com)"  # Replace with your details
wiki_wiki = wikipediaapi.Wikipedia(user_agent=user_agent, language="en")

summarizer = pipeline("summarization")

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
        full_text = page.text[:1000]
        try:
            summary = summarizer(full_text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
            answer = f"Here's a summary about '{question}': {summary}"
        except Exception as e:
            summary = page.summary[:500] + "..."
            answer = f"Here's what I found about '{question}': {summary}"
    else:
        answer = "I couldn't find any information on that topic. Can you clarify?"

    return jsonify({'answer': answer})

    return jsonify({'answer': answer})
if __name__ == '__main__':
    app.run(debug=True)