from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required,Email


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Post Comment')

class BlogForm(FlaskForm):
    topic = StringField('Topic',validators=[Required()])
    pitch = TextAreaField('Blog Content:', validators=[Required()])
    submit = SubmitField('Submit')

