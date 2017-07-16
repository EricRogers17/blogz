from flask import Flask, redirect, request, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['DEBUG'] = True
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blogz:blogzapp@localhost:8889/blogz'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'something'


class Blog(db.Model):
    ''' Organizes a blog post by sections defined below '''

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(120))
    publish_date = db.Column(db.DateTime)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.publish_date = datetime.utcnow()
        self.owner = owner


class User(db.Model):
    '''Will create and store new users '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    blogs = db.relationship('Blog', backref='owner')

    def __init__(self, username, password):
        self.username = username
        self.password = password


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']

    # Error variables
    username_error = ''
    password_error = ''
    verify_error = ''

    # ---- Validate user signup -----
    # username and password musn't have spaces and be between 3-20 characters
    if len(username) < 3 or len(username) > 20:
        username_error = 'Username must be between 3-20 charaters'

    if ' ' in username:
        username_error = 'Username cannot contain spaces'

    if len(password) < 3 or len(password) > 20:
        password_error = 'Password must be between 3-20 charaters'

    if ' ' in password:
        password_error = 'Password cannot contain spaces'

    # user's password and verify don't match
    if password != verify:
        verify_error = "Password and Verify Password don't match"

    # Query db to check for an existing user
    existing_user = User.query.filter_by(username=username).first()
    if not existing_user:
        new_user = User(username, password)
        db.session.add(new_user)
        db.session.commit()
        session['username'] = username
        return redirect('/index.html')
    else:
        return render_template('signup.html',
                               username=username,
                               username_error=username_error,
                               password_error=password_error,
                               verify_error=verify_error,
                               )


@app.route('/blog')
def display_blogs():
    blog_id = request.args.get('id')

    if (blog_id):
        blog = Blog.query.get(blog_id)
        return render_template('one_blog.html', page_title="Blog Entry", blog=blog)

    sort_type = request.args.get('sort')
    if sort_type == "newest":
        blogs = Blog.query.order_by(Blog.created.desc()).all()
    else:
        blogs = Blog.query.all()

    return render_template('index.html', blogs=blogs)


@app.route('/newpost')
def display_newpost_view():
    return render_template('newpost.html')


@app.route('/newpost', methods=['POST', 'GET'])
def add_post():
    # Will probably need this when creating new posts:
    #owner = User.query.filter_by(email=session['email']).first()

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
        url = "/blog?id=" + str(new_blog.id)
        return redirect(url)
    else:
        return render_template('newpost.html', title_error=title_error, body_error=body_error)


if __name__ == '__main__':
    app.run()
