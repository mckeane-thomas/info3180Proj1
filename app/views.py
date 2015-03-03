"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
import os
from app import app
from flask import render_template,request,redirect,url_for,flash, session,jsonify, send_from_directory
from app.forms import RegisterForm
from werkzeug import secure_filename
from app import db
from app.models import  ProfileData
import time, string


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

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
      if form.validate_onSubmit():
         name = request.form['username']
         fname = request.form['fname']
         lname = request.form['lname']
         age = request.form['age']
         sex = request.form['sex']
         high_score=request.form['high_score']
         profile_add_on = dateAdded()
         tDollars = request.form['tDollars']
      
         file = request.files['file']
         if file and file_allowed(file.filename):
            filename = name+'_'+secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
      
         newprofile =  ProfileData(name,filename,fname,lname,age,sex,profile_add_on,high_score,tDollars)
      
         db.session.add(newprofile)
         db.session.commit()
      #session['user_id']=user.id
         return "Registration Completed values added to the database"  
         flash("New Profile added")
      else:
         return("Profile could not be Created Fill in required fields")
   #else:  
   #return redirect(url_for('home'))
   return render_template("profile_add.html", form=form) 
   
def file_allowed(filename):
   return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

def dateAdded():
   date_add=time.strftime("%a  %d  %b  %Y")
   return date_add
  
@app.route('/profiles/', methods =['POST', 'GET'])
def profile_list():
   if request.method=='POST':
      all_users =  ProfileData.query.all()
      results = []
      for user in all_users:
         d ={'username': user.username, 'userid': user.id}
         results.append(d)
      return jsonify(users=results)
   #route for adding a profile
   else:
      list_profiles =  ProfileData.query.all()
      """adding a profile single Profile."""
      
   return render_template("profiles.html", list_profiles=list_profiles) 
  
@app.route('/profile/<int:id>/', methods =['GET','POST'])
def single_profile(id):
   results =  ProfileData.query.get(id)
   prof_added = results.profile_add_on
   format_date = prof_added.strftime("%a, %d %b %Y")
   img = profile_image(results)
   if request.method =="POST":
      return jsonify(userid=results.id,
                     username=results.username,
                     image=results.img,
                     sex=results.sex,
                     age=results.age,
                     profile_add_on=str(format_date),
                     high_score=results.high_score,
                     tDollars=results.tDollars)
   else:
      return render_template("profile_view.html", results=results,time=format_date,img=img)
    #route for viewing a profile by id
    #return "profile {}".format(id)


def profile_image(filename):
   return url_for('static',filename='img/'+ filename.img )
   


if __name__ == '__main__': 
    app.run(debug=True,host="0.0.0.0",port="9999")
