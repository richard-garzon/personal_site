from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    conf = {
        'twitter_url': 'http://twitter.com/gzgzgz____',
        'linkedin_url': 'http://linkedin.com/in/garzonr',
        'github_url': 'http://github.com/murdoc02'
    }
    return render_template('index.html',title='Home', conf=conf)
