from flask import Flask, render_template, request, url_for
from jenkins_config import *
from lib import *
import json

class Args:
    def __init__(self, release=None, job=None, yaml=None, context=None):
        self.release = release
        self.job = job
        self.yaml = yaml
        self.context = context

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/github', methods=['POST'])
def github():
    args = Args(release=request.form['release'])
    return json.dumps(build_yaml(args, github_token))
