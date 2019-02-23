from flask import render_template,request,redirect,url_for
from . import main
from datetime import datetime
from time import time, sleep
from .forms import BlogForm, CommentForm
from ..models import User, Blog, Comment
from flask_login import login_required, current_user

import requests
import json

# Views
@main.route('/')
def index():

    title = 'Home - Blog App'
    return render_template("index.html", title=title)

@main.route('/new_blog',methods = ['GET', 'POST'])
@login_required
def new_blog():

    blog_form = BlogForm()


    if blog_form.validate_on_submit():
        topic = blog_form.topic.data
        pitch = blog_form.pitch.data

        new_pitch = Blog(blogs_topic = topic, blogs_content=pitch, blogs_posted_on = datetime.now() , user = current_user)
        new_pitch.save_blog()
        return redirect(url_for('main.new_blog'))


    all = Blog.get_all_blogs()

    return render_template("new_blog.html", pitch_form = blog_form, pitches = all)

@main.route('/blogs')
def blogs():


    random = requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()
    all_pitches = Blog.get_all_blogs()
    return render_template("blogs.html",pitches = all_pitches,random = random)

@main.route('/comments/<int:id>',methods = ['GET','POST'])
def pitch(id):

    my_pitch = Blog.query.get(id)
    comment_form = CommentForm()

    if comment_form.validate_on_submit():
        comment_data = comment_form.comment.data
        new_comment = Comment(c_content = comment_data, c_blog_id = id, c_com_posted_on = datetime.now())
        new_comment.save_comment()

        return redirect(url_for('main.pitch',id=id))

    all_comments = Comment.get_comments(id)

    title = 'Comment Section'
    return render_template('comment.html',pitch = my_pitch, comment_form = comment_form, comments = all_comments, title = title)
