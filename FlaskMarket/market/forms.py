from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label = "User Name:")
    email_adress = StringField(label = "Email Adress:")
    password1 = PasswordField(label = "Password:")
    password2 = PasswordField(label = "Confirm Password:")
    submit = SubmitField(label = "submit")