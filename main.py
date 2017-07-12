from flask import Flask, redirect, request, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:rogers@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'something'


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(120))

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/blog')
def index():
    return render_template('index.html')


@app.route('/blog', methods=['POST', 'GET'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']


@app.route('/newpost', methods=['POST', 'GET'])
def newpost():
    if request.method == 'POST':
        title = request.form('title')
        body = request.form('body')

    # if title == '':
    #    flash('Please fill out the title field')
    # if not body:
    #    flash('Please fill out the body field')
    return render_template('newpost.html')
if __name__ == '__main__':
    app.run()
