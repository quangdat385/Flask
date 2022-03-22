

from flask import Flask,render_template,flash,request
from flask_wtf import FlaskForm 
from wtforms import StringField,SubmitField,PasswordField,BooleanField,ValidationError
from wtforms.validators import DataRequired,EqualTo,Length
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash,check_password_hash


app= Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///users.db'


app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://root:783151@localhost/our_users"

app.config["SECRET_KEY"] = "my supper secret key that no one is supposed to know"
db=SQLAlchemy(app)
migrate=Migrate(app,db)



@app.route("/date")
def run_file_python():
    return {"Date":date.today()}

class Users(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(120),nullable=False,unique=True)
    favorite_color=db.Column(db.String(120))
    date_added=db.Column(db.DateTime,default=datetime.utcnow)
    
    password_hash=db.Column(db.String(128))
    @property
    def password(self):
        raise AttributeError("password id not readable attribute!")
    @password.setter
    def password(self, password):
        self.password_hash= generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
    
    def __repr__(self):
        return '<Name %r>' % self.name
@app.route('/delete/<int:id>')
def delete(id):
    user_to_delete=Users.query.get_or_404(id)
    name=None   
    form = UserForm()
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash('User Deleteed Successfully')
        our_users=Users.query.order_by(Users.date_added)
        return render_template("add_user.html",
                        form=form,
                        name=name,
                        our_users=our_users)
    
    except:
        flash('Whoops! There was a problem deleting user , try again')
        return render_template("add_user.html",
                        form=form,
                        name=name,
                        our_users=our_users)
#Form
class UserForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired()])
    favorite_color=StringField("Favorite Color")
    password_hash = PasswordField("Password",validators=[DataRequired(),
                    EqualTo("password_hash2",message="Passwords Must Match!")])
    password_hash2 = PasswordField("Confirm Password",validators=[DataRequired()])
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
        name_to_update.password_hash=request.form["password_hash"]
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
                                name_to_update=name_to_update,
                                id=id)
    
@app.route('/user/add',methods=["GET","POST"])
def add_user():
    name=None
    form =UserForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user is None:
            hashed_pw=generate_password_hash(form.password_hash.data,"sha256")
            user=Users(name=form.name.data,email=form.email.data,
                    favorite_color=form.favorite_color.data,
                    password=hashed_pw)
            db.session.add(user)
            db.session.commit()
        name=form.name.data
        form.name.data=""
        form.email.data =""
        form.favorite_color.data =""
        form.password_hash.data =""
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
# pip install Flask-Migrate
# flask db init 
# flask db migrate -m "Initial Migration"
# flask db upgrade
# flask shell
# from main import Users
# u=Users()
# u.password="cat"
# u.password
# u.password_hash
# u.verify_password("cat)