from flask import render_template, request, redirect, url_for
app = views.app

#検証用DB
users = {'user1': 'password1', 'user2': 'password2'}

@app.route('/')
def home():
    return "welcome to the Home Page!!"

@app.rote('/login', method =[ 'GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        