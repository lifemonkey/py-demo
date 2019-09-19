from flask import *
from flask_mail import *
from random import *
from email_validator import validate_email, EmailNotValidError
import hqd.flask.database as mysql_db

app = Flask(__name__, template_folder='templates')
app.secret_key = 'test secret key'

# CONFIGURATION
# Flask-mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'hqd.auto.sender@gmail.com'
app.config['MAIL_PASSWORD'] = 'Learnbyheart8h'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
# Instantiate the Mail class
mail = Mail(app)
otp = randint(000000, 999999)


# IMPLEMENTATION
@app.route('/')
def main():
    flash("")
    return render_template('login.html')


@app.route('/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    db = mysql_db.Database()

    if db.verify_user(username, password) is True:
        flash("You are successfully logged in")
        # Create session data, we can access this data in other routes
        session['logged_in'] = True
        session['username'] = username
        # Redirect to account page
        return redirect(url_for('account'))

    msg = 'Incorrect username/password!'
    return render_template('login.html', msg=msg)


@app.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # Check if account exists using MySQL
        db = mysql_db.Database()
        msg = db.add_user(username, password, email)

    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)


@app.route('/logout')
def logout():
    if not session.get('logged_in'):
        return "Not logged in"
    else:
        # Remove session data, this will log the user out
        session.pop('logged_in', None)
        session.pop('username', None)
        # Redirect to login page
    return render_template('login.html')


@app.route('/account')
def account():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('account.html')


@app.route('/verify', methods=['POST'])
def verify():
    email = request.form.get('email', None)
    try:
        validate_email(email)
        msg = Message('Activation code', sender='hqd.auto.sender@gmail.com', cc='h.doan@laudert.de', recipients=[email])
        msg.body = 'Hi there, this is the mail sent by using the flask web application. Your activation code is ' + str(otp)
        mail.send(msg)
        return render_template('verify.html', email=email)
    except EmailNotValidError:
        flash("Email is not valid")
        return redirect(url_for('account'))


@app.route('/validate', methods=["POST"])
def validate():
    user_otp = request.form['otp']
    if otp == int(user_otp):
        return "<h3>Email verified successfully</h3>"
    return "<h3>failure</h3>"


@app.route('/success', methods=['POST', 'GET'])
def success():
    if request.method == 'POST':
        result = ""
        data = request.form
        for key, value in data.items():
            result += key + ": " + value + "\t"
        if result is "":
            data = request.files['file']
            data.save(data.filename)
            result += "File name: " + data.filename

        return render_template('success.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
