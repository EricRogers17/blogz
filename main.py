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
    blogs = Blog.query.all()
    return render_template('index.html', blogs=blogs)


@app.route('/newpost')
def display_newpost_view():
    return render_template('newpost.html')


@app.route('/newpost', methods=['POST', 'GET'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

    title_error = ''
    body_error = ''

    if title == '':
        title_error = 'Please fill out the Title field'
    if body == '':
        body_error = 'Please fill out the Blog field'

    if not title_error and not body_error:
        new_blog = Blog(title, body)
        db.session.add(new_blog)
        db.session.commit()
        return redirect('/blog')
    else:
        return render_template('newpost.html', title_error=title_error, body_error=body_error)


if __name__ == '__main__':
    app.run()
