from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba236'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gaming.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    password = db.Column(db.String(60),nullable=False)



    def __repr__(self):
        return f"User('{self.username}','{self.email}')"


class Game(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100),nullable=False)
    platforms = db.Column(db.String(100),nullable=False)
    theme = db.Column(db.String(50),nullable=False)
    genre = db.Column(db.String(50),nullable=False)
    summary = db.Column(db.Text,nullable=False)
    rating = db.Column(db.Integer,nullable=False)


    def __repr__(self):
        return f"Game('{self.title}','{self.summary}')"



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')





@app.route('/createaccount',methods = ['GET','POST'])
def createaccount():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data} !','success' )
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form = form)




@app.route('/connexion',methods = ['GET','POST'])
def connexion():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("You have been logged in!","success")
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, Please check username and password','danger')
    return render_template('login.html', title = 'Login', form = form)



@app.route('/newpassword')
def newpassword():
    return render_template('newpassword.html')


@app.route('/search')
def search():
    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)
