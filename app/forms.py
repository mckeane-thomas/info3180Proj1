#from flask.ext.uploads import UploadSet, IMAGES
from flask.ext.wtf import Form
from wtforms.fields import TextField, IntegerField, DateField, RadioField
from wtforms.validators import Required, Optional
from flask_wtf.file import FileField, FileAllowed, FileRequired
 
class RegisterForm(Form):
      #profile_photo =FileField('Profile Image')
	userID =IntegerField('ID:', [Required()])
	username = TextField('Username:', [Required()])
	upload = FileField('image', validators=[FileRequired(),FileAllowed(images, 'Images only!')])
	firstName = TextField('First Name:', [Required()])
	lastName = TextdField('Last Name:', [Required()])
	sex = RadioField(u'Sex', choices=[
        ('M', u'Male'),
        ('F', u'Female')],
        default='M', validators=[Required()])
	age = IntegerField('Age:', [Required()])
	profile_add_on = DateField('Profile Created',[validators.required()])
	high_score = IntegerField('High Score', [Optional()])
	tdollars = IntegerField('TDollars', [Optional()])
