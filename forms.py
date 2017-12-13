from flask_wtf import Form
from wtforms import StringField,PasswordField,SubmitField,SelectField
from wtforms import ValidationError,validators
from wtforms.validators import input_required,equal_to


class LoginForm(Form):
    username = StringField("Username",validators=[input_required()]);
    password = PasswordField("Password",validators = [input_required()]);
    submit = SubmitField("Login");


class RegisterForm(Form):
    Firstname = StringField("Firstname",validators=[input_required()]);
    Lastname  = StringField("Lastname",validators=[input_required()]);
    Username = StringField("Username",validators=[input_required("Enter username")]);
    Email = StringField("Email",validators=[input_required("Email required")]);
    Password = PasswordField("Password",validators=[input_required("Password required")]);
    Confirm = PasswordField("Confirm Password",validators=[input_required("Re-enter password"),
                                                           equal_to("Password",message="passwords don't match")]);
    submit = SubmitField("Submit");

class Authentication2(Form):
    Code = PasswordField("Enter code here",validators=[input_required()]);
    Submit = SubmitField("Submit");


