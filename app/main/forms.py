from wtforms import Form, TextAreaField, SubmitField, FileField, BooleanField
from wtforms.validators import InputRequired


class UserForm(Form):
    message = TextAreaField('Enter your message:')
    template = BooleanField('Use a template?')
    file = FileField('Choose the file:')
    submit = SubmitField('Submit')
