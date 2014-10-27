#-*- coding: UTF-8 -*- 
from flask import Flask, render_template, request, redirect, url_for, abort, session
import crawler

app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34D';
app.debug=True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    #session['username'] = request.form['username']
    session['message'] = request.form['message']
    return redirect(url_for('message'))

@app.route('/message')
def message():
    
   try: 
    return render_template('resume.html', message=crawler.GetInfo(session['message']),message_user=session['message'])
   except EnvironmentError:
   	return render_template('index.html')
from bae.core.wsgi import WSGIApplication  
application = WSGIApplication(app)  


