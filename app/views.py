"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app
from flask import render_template,request,redirect,url_for,flash, session
from app.forms import RegisterForm
from app import db
from app.models import Profile
import time


###
# Routing for your application.
###

@app.route('/',methods=['GET'])
def home():
   """Render the website's about page."""
   return render_template('home.html')
    


@app.route('/about/')
def about():
   """Render the website's about page."""
   return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
   """Send your static text file."""
   file_dot_text = file_name + '.txt'
   return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
   """Custom 404 page."""
   return render_template('404.html'), 404
    

@app.route('/profile/', methods=['POST','GET'])
def profile_add():
   #route for adding a profile
   """adding a profile single Profile."""
   form = RegisterForm()
   if request.method == 'POST':
      #write to the database
      
      username = request.form['username']
      img = request.form['img']
      fname = request.form['fname']
      lname = request.form['lname']
      age = request.form['age']
      sex = request.form['sex']
      high_score=request.form['high_score']
      profile_add_on = dateAdded()
      tDollars = request.form['tDollars']
      
      #check if user is already created
      isUser = Profile.query.filter_by(username).first()
      if(isUser is None):
         newprofile = Profile(username,img,fname,lname,age,sex,profile_add_on,high_score,tDollars)
         
         db.session.add(newprofile)
         db.session.commit()
         #session['user_id']=user.id
         return "Registration Completed values added to the database"  
         flash("New Profile added")
      else:
         flash("Profile could not be Created, Username Already Exist")
   else:  
      #return redirect(url_for('home'))
      return render_template("profile_add.html", form=form) 

def dateAdded():
   date_add=time.strftime("%a,%d,%b,%Y")
   return date_add
  
@app.route('/profiles/')
def profile_list():
   #route for adding a profile
   """adding a profile single Profile."""
      
   return render_template("profiles.html", form=form) 
  
@app.route('/profile/<int:id>/')
def single_profile(id):
    #route for viewing a profile by id
    return "profile {}".format(id)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="9999")
