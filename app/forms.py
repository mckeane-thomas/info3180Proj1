from flask import Flask
from flask.ext.wtf import Form
from wtforms.fields import TextField, IntegerField, DateField, RadioField
from wtforms.validators import Required, Optional
from flask_wtf.file import FileField, FileAllowed, FileRequired
 
#images = UploadSet('images', IMAGES)

class RegisterForm(Form):
      #profile_photo =FileField('Profile Image')
	userID =IntegerField('ID:', [Required()])
	username = TextField('Username:', [Required()])
	upload = FileField('image', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])
	firstName = TextField('First Name:', [Required()])
	lastName = TextField('Last Name:', [Required()])
	sex = RadioField(u'Sex', choices=[
        ('M', u'Male'),
        ('F', u'Female')],
        default='M', validators=[Required()])
	age = IntegerField('Age:', [Required()])
	profile_add_on = DateField('Profile Created',[Required()])
	high_score = IntegerField('High Score', [Optional()])
	tdollars = IntegerField('TDollars', [Optional()])