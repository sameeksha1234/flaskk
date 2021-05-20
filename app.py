
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy



app= Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/db_name' 
db= SQLAlchemy(app)

class Contacts(db.Model):
    slno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.String(120), nullable=False)

 


@app.route("/")
def home():
    return render_template('Home.html')

@app.route("/About_Covid")
def About_Covid():
    return render_template('About_Covid.html')



@app.route("/Covid_Forecast")
def Covid_Forecast():
    return render_template('Covid_Forecast.html')

@app.route("/Global_Trend")
def Global_Trend():
    return render_template('Global_Trend.html')

@app.route("/India_Trend")
def India_Trend():
    return render_template('India_Trend.html')

@app.route("/Karnataka_Trend")
def Karnataka_Trend():
    return render_template('Karnataka_Trend.html')
@app.route("/Test_Yourself")
def about():
    return render_template('Test_Yourself.html')

@app.route("/Contact", methods = ['GET','POST'])
def contacts(): 
    if(request.method=='POST'): 
        name= request.form.get('name')
        email= request.form.get('email')
        message= request.form.get('message') 
        entry= Contacts(name=name, email=email, message=message)
        db.session.add(entry)
        db.session.commit()
    return render_template('Contact.html')


app.run(debug=True)