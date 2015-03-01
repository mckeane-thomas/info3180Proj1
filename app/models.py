from . import db

class dataProfile(db.Model):
        id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), unique=True)
	img = db.Column(db.bytea(50))
        fname = db.Column(db.String(50))
        lname = db.Column(db.String(50))
        age = db.Column(db.Integer)
        sex=db.Column(db.String(10))
	profile_add_on=db.Column(db.Date)
	high_score =db.Column(db.Integer)
	tDollars =db.Column(db.Integer)
	


	def __init__(self,username,img,fname,lname,age,sex,profile_add_on,high_score,tDollars):
	   #self.userid = userid
	   self.username=username 
	   self.img = img
	   self.fname = fname
           self.lname = lname
           self.age = age
           self.sex = sex
           self.profile_add_on=profile_add_on
           self.high_score=high_score
           self.tDollars=tDollars
           
          
           

        def __repr__(self):
	    return '<dataProfile %r %r>' %(self.fname, self.lname)
