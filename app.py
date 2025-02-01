from flask import Flask, request, render_template, redirect
import yaml
import requests

app = Flask(__name__)
data = []

def load_data():
    with open('data/results.yaml') as f:
        return yaml.safe_load(f)

@app.route('/')
def index():
    query = request.args.get('q', '')
    filtered_data = [item for item in data if (query.lower() in item['name'].lower() or query.lower() in ' '.join(item['tags']))]
    return render_template('index.html', results=filtered_data, query=query)

@app.route('/results')
def results():
    return redirect('/')

if __name__ == '__main__':
    data = load_data()
    app.run(debug=True)
