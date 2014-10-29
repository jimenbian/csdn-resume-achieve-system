#-*- coding: UTF-8 -*- 
from flask import Flask, render_template, request, redirect, url_for, abort, session
import crawler
import mysql_manager
import evaluate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34D';
app.debug=True

@app.route('/')
def home():
   #mysql_manager.sql_connect()
    
   return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    #session['username'] = request.form['username']
    session['message'] = request.form['message']
    return redirect(url_for('message'))

@app.route('/message')
def message():
    
  try:
    #score=evaluate.get_score(crawler.GetInfo(session['message'])[0],crawler.GetInfo(session['message'])[3],crawler.GetInfo(session['message'])[6])    
    #mysql_manager.add_data(str(session['message']))
    return render_template('resume.html', message=crawler.GetInfo(session['message']),message_user=session['message'])
  except EnvironmentError:
   	return render_template('index.html')

from bae.core.wsgi import WSGIApplication  
application = WSGIApplication(app)  

# if __name__ == '__main__':
#     app.run()
