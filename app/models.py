from app import db

class User(db.Model):
	__tablename__ = 'users_user'
        userid = db.Column(db.Integer,nullable = False, primary_key=True)
	userName = db.Column(db.String(50), Unique=True)
	img = db.Column(db.LargeBinary)
        fname = db.Column(db.String(50), unique=True)
        lname = db.Column(db.String(50), unique=True)
        sex=db.Column(db.String(10))
	age = db.Column(db.Integer)
	profile_add_on=db.Column(db.DateTime)
	high_score =db.Column(db.Integer)
	tDollars =db.Column(db.Integer)
	


	def __init__(self, userid, username, img,fname, lname,, profile_add_on,sex,age):
	   self.userid = userid
	   self.username=username 
	   self.img = img
	   self.fname = fname
           self.lname = lname
           self.profile_add_on=profile_add_on
           self.sex = sex
           self.age = age
          
           

        def __repr__(self):
	    return '<User %r>' %(self.username)
