

from flask import Flask,render_template,flash,request
from flask_wtf import FlaskForm 
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate

app= Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///users.db'


app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://root:783151@localhost/our_users"

app.config["SECRET_KEY"] = "my supper secret key that no one is supposed to know"
db=SQLAlchemy(app)
migrate=Migrate(app,db)




class Users(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(120),nullable=False,unique=True)
    favorite_color=db.Column(db.String(120))
    date_added=db.Column(db.DateTime,default=datetime.utcnow)
    
    def __repr__(self):
        return '<Name %r>' % self.name

#Form
class UserForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired()])
    favorite_color=StringField("Favorite Color")
    submit=SubmitField("Submit")
class NamerForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    
    submit=SubmitField("Submit")
    
@app.route("/update/<int:id>",methods=["GET", "POST"])
def update(id):
    form = UserForm()
    name_to_update =Users.query.get_or_404(id)
    if request.method == "POST":
        name_to_update.name=request.form["name"]
        name_to_update.email=request.form["email"]
        name_to_update.favorite_color=request.form["favorite_color"]
        try :
            db.session.commit()
            flash("User updated successfully")
            return render_template("update.html", 
                                form=form ,  
                                name_to_update=name_to_update)
        except:
            flash("Error ! Looks like there was a problem ...try again!")
            return render_template("update.html", 
                                form=form ,  
                                name_to_update=name_to_update)
    else:   
        return render_template("update.html", 
                                form=form ,  
                                name_to_update=name_to_update)
    
@app.route('/user/add',methods=["GET","POST"])
def add_user():
    name=None
    form =UserForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user=Users(name=form.name.data,email=form.email.data,
                    favorite_color=form.favorite_color.data)
            db.session.add(user)
            db.session.commit()
        name=form.name.data
        form.name.data=""
        form.email.data =""
        form.favorite_color.data =""
        flash("User Added Successfully")
    our_users=Users.query.order_by(Users.date_added)
    return render_template("add_user.html",
                        form=form,
                        name=name,
                        our_users=our_users)
    
@app.route('/')

def index():
    # safe
    # capitalize
    # lower
    # upper 
    # title
    # trim 
    # striptags
    first_name="Nguyen"
    # stuff= "This Is <strong> Bold </strong>Text"
    stuff= "This Is bold Text"
    flash("Welcom To Our Website!")
    favorite_pizza=["Pepperoni","Cheese","Mushrooms",41]
    
    
    return render_template("index.html",first_name=first_name,
                            stuff=stuff,
                            favorite_pizza=favorite_pizza,
                            )
    

# def index():
#     return "<h1> Hello World !!</h1>"
@app.route('/user/<name>')
def user(name):
    return render_template("user.html",user_name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500

@app.route('/name',methods=["GET", "POST"])
def  name():
    name=None
    form =NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data=""
        flash("Form submitted Successfully")
    return render_template("name.html",
                            name=name,
                            form=form)



if __name__== '__main__':
    app.run(debug=True)
    
#ssh-keygen.exe
# cat id_rsa.pub
# git config --global user.name "Dat Nguyen"
# git config --global user.email "cddd4f@yahoo.com"
# git config --global push.default matching
# git config --global alias.co checkout
# git init
# source "d:/khoa k03/Flask/virt/Scripts/activate"
# touch .gitignore
# git remote add origin https://github.com/quangdat385/quangdat385.git
# 
# 
# git push -u origin main'
# git add .
# git commit -am "tweaked 500.html"

# git pull
#  git push

# run flask
# export FLASK_ENV=development
# export FLASK_APP=main.py
# flask run
