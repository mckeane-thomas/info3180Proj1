"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for
from app import app
from flask import render_template,request,redirect,url_for
from app.forms import RegisterForm
from app import db
from app.models import User


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
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
    
#route for adding a profile
@app.route('/profile',methods=['GET'])
def profile():

  """adding a profile single Profile."""
  form = RegisterForm(request.form)
  if form.validate_on_submit():
     user = User(userid = form.userid.data, username=form.username.data, img=form.img.data,fname=form.fname.data,lname=form.lname.data,sex=form.sex.data,age=form.age.data,profile_add_on=form.profile_add_on.data)
     db.session.add(user)
     db.session.commit()

     session['user_id']=user.id

     flash('You have been registered')
    
     return redirect(url_for('home'))
  return render_template("profile.html", form=form)    
    


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")