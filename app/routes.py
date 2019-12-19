from flask import render_template
from flask import request
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/search')
def search():
    q = request.args.get('q')
    results = []
    return render_template('search.html', q = q, results = results )