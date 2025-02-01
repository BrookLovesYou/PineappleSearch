import requests
from flask import Flask, request, render_template, jsonify, url_for
import yaml
from urllib.parse import urlparse
from bs4 import BeautifulSoup

app = Flask(__name__)
data = []

def load_data():
    with open('data/results.yaml') as f:
        return yaml.safe_load(f)

def ping_url(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return 'Up'
        else:
            return 'Down ({})'.format(response.status_code)
    except requests.RequestException as e:
        return 'Down (Error: {})'.format(e)

@app.route('/')
def index():
    query = request.args.get('q', '')
    filtered_data = [item for item in data if (query.lower() in item['name'].lower() or query.lower() in ' '.join(item['tags']))]
    
    # Add ping status to each result
    for item in filtered_data:
        item['status'] = ping_url(item['url'])
    
    return render_template('index.html', results=filtered_data, query=query)

@app.route('/suggest')
def suggest():
    query = request.args.get('q', '').lower()
    suggestions = []
    for item in data:
        if query in item['name'].lower() or query in ' '.join(item['tags']).lower():
            suggestions.append(item['name'])
    return jsonify(suggestions[:5])  # Limit to 5 suggestions

if __name__ == '__main__':
    data = load_data()
    app.run(host='0.0.0.0', port=5000)
