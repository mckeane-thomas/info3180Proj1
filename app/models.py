from app import db

class Profile(db.Model):
        id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), unique=True)
	img = db.Column(db.LargeBinary)
        fname = db.Column(db.String(50), unique=True)
        lname = db.Column(db.String(50), unique=True)
        sex=db.Column(db.String(10))
	age = db.Column(db.Integer)
	profile_add_on=db.Column(db.DateTime)
	high_score =db.Column(db.Integer)
	tDollars =db.Column(db.Integer)
	


	def __init__(self,username,img,fname, lname,profile_add_on,sex,age,high_score,tDollars):
	   #self.userid = userid
	   self.username=username 
	   self.img = img
	   self.fname = fname
           self.lname = lname
           self.profile_add_on=profile_add_on
           self.sex = sex
           self.age = age
           self.high_score=high_score
           self.tDollars=tDollars
           
          
           

        def __repr__(self):
	    return '<Profile %r %r>' %(self.fname, self.lname)
