"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app
from flask import render_template,request,redirect,url_for, Blueprint,flash, g, session
from app.forms import RegisterForm
from app import db
from app.models import User


###
# Routing for your application.
###

app.config['SECRET_KEY']="sdfhdjksfhgm nm,sfnjkdfsbdjbfkjsbbjasbhdsbfd"


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
   #form = RegisterForm(request.form)
   if request.method =="POST":
      #write to the database
      #img = request.form['img']
      
      username = request.form['username']
      fname = request.form['fname']
      lname = request.form['lname']
      sex = request.form['sex']
      age = request.form['age']
      high_score=request.form['high_score']
      tDollars = request.form['tDollars']
      #profile_add_on = request.form['profile_add_on']
   user = User(username,fname,lname,sex,age,high_score,tDollars)
      #user = User(username=form.username.data, fname=form.fname.data,lname=form.lname.data, sex=form.sex.data, age=form.age.data, high_score=form.high_score.data, tDollars=form.tDollars.data)
      db.session.add(user)
      db.session.commit()

      #session['user_id']=user.id
      return "Registration Completed values added to the database"  
      flash('You have been registered')
    
      return redirect(url_for('home'))
   return render_template("profile_add.html", form=form) 
  
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
