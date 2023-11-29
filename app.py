from flask import Flask, render_template
# from forms import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secretkey"

@app.route('/')
def index():
    
    ####### Home page #########
    
  

    return render_template('index.html')

# @app.route('/name')
# def name():
#     return render_template('name.html')


# @app.route('/login', methods=['GET', 'POST'])
# def login():
    
#     ####### Login Page ###########
    
#     # name = None
#     # form = LoginForm()
#     # if form.validate_on_submit():
#     #     name = form.name.data
#     #     form.name.data = ''
        
#         return render_template('login.html')


# @app.route('/logout')
# def logout():
    
#     ######## Logout Page ##########
    
    
#     return render_template('logout.html')


# @app.route('/profile')
# def profile():
    
#     ####### Profile Page ##########
    
    
#     return render_template('profile.html')


# @app.route('/players')
# def players():
    
#     ######## Players Page ##########
    
    
#     return render_template('players.html')


###### Invalid URL ###########

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


