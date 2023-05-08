from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User

# formulaire de login : 
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

# formulaire de création de compte :
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Password Confirmation', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registration')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        # je vérifie que ce nom n'est pas déjà présent en bdd : 
        if user is not None:
            raise ValidationError('Please enter a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        # je vérifie que ce nom n'est pas déjà présent en bdd : 
        if user is not None:
            raise ValidationError('Please enter a different email address.')
        
# formulaire de profil :
class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About Me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')
