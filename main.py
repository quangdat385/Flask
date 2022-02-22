
from flask import Flask,render_template,flash
from flask_wtf import FlaskForm 
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app= Flask(__name__)
app.config["SECRET_KEY"] = "my supper secret key that no one is supposed to know"
#Form
class NamerForm(FlaskForm):
    name = StringField("What's Your Name",validators=[DataRequired()])
    submit=SubmitField("Submit")
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
                            favorite_pizza=favorite_pizza)
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
