
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, redirect, jsonify, url_for, g

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')
    
@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/lovelive')
def lovelive():
    return render_template('lovelive.html')

if __name__ == '__main__':
    app.run()
