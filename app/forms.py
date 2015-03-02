from flask import Flask
from flask.ext.wtf import Form
#from flask.ext.uploads import UploadSet, IMAGES
from wtforms.fields import TextField, IntegerField, DateField, RadioField
from wtforms.validators import Required, Optional
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flaskext.uploads import UploadSet, IMAGES
 
#images = UploadSet('images', IMAGES)

class RegisterForm(Form):
      #profile_photo =FileField('Profile Image')
	userid =IntegerField('ID:', [Required()])
	username = TextField('Username:', [Required()])
	#img = FileField('image', validators=[Optional(),FileAllowed(['jpg', 'png'], 'Images only!')])
	fname = TextField('First Name:', [Required()])
	lname = TextField('Last Name:', [Required()])
	sex = RadioField(u'Sex', choices=[
        ('M', u'Male'),
        ('F', u'Female')],
        default='M', validators=[Required()])
	age = IntegerField('Age:', [Required()])
	profile_add_on = DateField('Profile Created',[Required()])
	high_score = IntegerField('High Score', [Optional()])
	tDollars = IntegerField('TDollars', [Optional()])
