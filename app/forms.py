from flask.ext.uploads import UploadSet, IMAGES
from wtforms import TextField, IntegerField, DateField
from wtforms.validators import Required, Optional, FileField, file_required
from flask_wtf.file import FileField, FileAllowed, FileRequired
 
class RegisterForm(Form):
      #profile_photo =FileField('Profile Image')
	userID =IntegerField('ID:', [Required()])
	username = TextField('Username:', [Required()])
	img = FileField('image', validators=[FileRequired(),FileAllowed(images, 'Images only!')])
	firstName = TextField('First Name:', [Required()])
	lastName = TextdField('Last Name:', [Required()])
	time_offset = RadioField(u'Label', choices=[
        ('2', u'Check when Daylight saving has begun, UTC+02:00'),
        ('1', u'Check when Daylight saving has stopped, UTC+01:00')],
        default='2', validators=[Required()])
	age = IntegerField('Age:', [Required()])
	profile_add_on = DateField('Profile Created',[validators.required()])
	high_score = IntegerField('High Score', [Optional()])
	tdollars = IntegerField('TDollars', [Optional()])
