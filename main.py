
from flask import Flask,render_template

app= Flask(__name__)

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
    
    favorite_pizza=["Pepperoni","Cheese","Mushrooms",41]
    return render_template("template.html",first_name=first_name,
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

if __name__== '__main__':
    app.run(debug=True)
# git config --global user.name "Dat Nguyen"
# git config --global user.email "cddd4f@yahoo.com"
# git config --global push.default matching
# git config --global alias.co checkout
# git init
# source "d:/khoa k03/Flask/virt/Scripts/activate"
# touch .gitignore