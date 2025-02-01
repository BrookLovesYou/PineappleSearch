import requests
from flask import Flask, request, render_template
import yaml

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

if __name__ == '__main__':
    data = load_data()
    app.run(debug=True)
