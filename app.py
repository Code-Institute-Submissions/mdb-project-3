import os
import datetime
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo, pymongo
from flask_login import current_user, login_user, LoginManager, login_required, logout_user
from bson.objectid import ObjectId
import re


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config["MONGO_DBNAME"] = 'myDB'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

login = LoginManager(app)
login.login_view = 'show_login'

conn=pymongo.MongoClient(os.getenv("MONGO_URI"))
DATABASE_NAME = 'myDB'
COLLECTION1 = 'account'
COLLECTION2 = 'gender'
COLLECTION3 = 'matches'
COLLECTION4 = 'profile'
COLLECTION5 = 'messages'
mongo = PyMongo(app)
class UserModel():
    id =""
    email = ""
    is_authenticated = False
    is_active= True
    is_anonymous= False
    def __init__(self, email, password, id):
        self.id = id
        self.email = email
        self.password = password
        self.is_authenticated = True
        self.is_active= True
        self.is_anonymous= False
    def get_id(self):
        return self.email

@login.user_loader
def load_user(email):
    check = conn[DATABASE_NAME][COLLECTION4].find_one({"email":email})
    user = UserModel(email, check["password"], check["_id"])
    return user

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
# ---allows authenticated users to see and delete matches---
    
@app.route('/get_matches')
@login_required
def get_matches():
    if current_user.is_authenticated:
        type = request.args.get('type')
        criteria= {} 
        
        if type and type != 'Type':
            criteria['gender'] = type
        else:
            type = 'Gender'
        
        gender = conn[DATABASE_NAME][COLLECTION2].find()
        matches = conn[DATABASE_NAME][COLLECTION3].find(criteria)
        return render_template('matches.html', matches=matches,gender=gender
        ,type=type)
    else:
        redirect("/login")
    
 
# redirects to the register page when user clicks Register link

@app.route('/register')
def show_register_form():
    return render_template('create-profile.html')

# ---Allows users to login into the site---

@app.route('/login', methods=['GET', 'POST'])
def show_login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        check = conn[DATABASE_NAME][COLLECTION4].find_one({"email":email
        , "password":password})
        if check:
            user = UserModel(email, password, check["_id"])
            login_user(user, remember=True)
            return redirect('/get_matches')
        else:
            return render_template('login.html'
            , message="invalid login")
    else:
        return render_template('login.html')
        
# ---allow users to send messages to database---
@login_required
@app.route('/messages/<profile_id>/<match_id>', methods=['GET','POST'])
def send_messages(profile_id, match_id):
    if request.method=='POST':
        check = conn[DATABASE_NAME][COLLECTION4].find({"_id":ObjectId(profile_id)})
        if check:
            messages = conn[DATABASE_NAME][COLLECTION5].insert({
                'timestamp': datetime.datetime.now(),
                'sender_id':  current_user.id,
                'recepient_id': ObjectId(profile_id),
                'message': request.form['message'],
                'match_id':ObjectId(match_id)
                })
            return render_template('send-messages.html', message = "Message sent to match!", profile_id=profile_id, match_id=match_id)
        else:
            return render_template('matches.html', message = "User not exist", profile_id=profile_id, match_id=match_id)
    return render_template('send-messages.html', profile_id=profile_id, match_id=match_id)
    

    
# Route does two things. 1. **Sends the user's information to the backend 
# and displays the profile in the profile page where they will be able
# to update their profile
    
@app.route('/register', methods=['GET', 'POST'])
def new_register_form():
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        gender = request.form['gender']
        bio = request.form['bio']
        email = request.form['email']
        password = request.form['password']

        check = conn[DATABASE_NAME][COLLECTION4].find({"email":email})
        if check.count() > 0:
            return render_template('create-profile.html'
            , message = "email already registered")
        conn[DATABASE_NAME][COLLECTION4].insert({
         "first_name": first_name,
         "last_name": last_name,
             "age": age,
             "gender":gender,
             "bio":bio,
             "email":email,
             "password": password,
         })
        
        return render_template('profile-page.html', fn=first_name, ln=last_name,  
          a=age,  g=gender, bio=bio)
    else:
        return render_template('create-profile.html')
        
# redirects the user to the update-profile page

@app.route('/updateNow')
def route_update_form():
    return render_template('update-profile.html')
 
      
# redirects the user to the profile page

@app.route('/profile')
def show_profile():
    return render_template('profile-page.html')
      
# When user updates their profile, they will be redirected to the profile page. 
        
@app.route('/update', methods=['POST'])
def show_update_form():
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        gender = request.form['gender']
        bio = request.form['bio']

        return render_template('profile-page.html', fn=first_name, ln=last_name,  
          a=age,  g=gender, bio=bio)
          



#delete individual match
#Adding a route to confirm if the user really wants to delete the match
@app.route('/matches/<matches_id>/confirm_delete')
def confirm_delete_matches(matches_id):
    matches = conn[DATABASE_NAME][COLLECTION3].find_one({
        '_id':ObjectId(matches_id)
    })
    return render_template('confirm_delete_matches.html', data=matches)
    
# # route that actually deletes the match
@app.route('/matches/<matches_id>/delete')
def delete_matches(matches_id):
    
    matches = conn[DATABASE_NAME][COLLECTION3].remove({
        '_id':ObjectId(matches_id)
        })
    
    # conn[DATABASE_NAME][COLLECTION3].remove({
    #     'matches_id'
    # })
    
    # flash("Match Has been deleted!")
    return redirect(url_for('index'))
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        
