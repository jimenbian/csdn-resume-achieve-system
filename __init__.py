##-*- coding: UTF-8 -*- 
from flask import Flask, render_template, request, redirect, url_for, abort, session
import main

app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34D';

@app.route('/')
def home():
    return render_template('GitHub Résumé.html')

@app.route('/signup', methods=['POST'])
def signup():
    #session['username'] = request.form['username']
    session['message'] = request.form['message']
    return redirect(url_for('message'))

@app.route('/message')
def message():
    a=main.GetInfo()[0]
    a1=main.GetInfo()[1]
    return render_template('message.html', message=a,message1=a1)

if __name__ == '__main__':
    app.run()


