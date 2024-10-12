from flask import Flask, request, jsonify, render_template
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.json
    query = data.get('query', '')
    response = process_query(query)
    return jsonify({'response': response})

def process_query(query):
    query = query.lower()
    if 'weather' in query:
        return get_weather()
    elif 'time' in query:
        return get_time()
    elif 'add' in query or 'plus' in query:
        numbers = extract_numbers(query)
        return f"The sum is {sum(numbers)}"
    else:
        return f"Sorry, I don't understand the query: {query}"

def get_weather():
    return "The weather is sunny."

def get_time():
    now = datetime.now()
    return f"The current time is {now.strftime('%H:%M:%S')}"

def extract_numbers(query):
    return [int(word) for word in query.split() if word.isdigit()]

if __name__ == '__main__':
    app.run(debug=True)
