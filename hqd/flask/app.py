from flask import *
from flask_mail import *
from random import *
from email_validator import validate_email, EmailNotValidError


app = Flask(__name__, template_folder='templates')
app.secret_key = 'test secret key'

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

# Users
users = {
    'admin': 'admin',
    'hqd': 'hqd',
}


@app.route('/')
def main():
    flash("")
    return render_template('home.html')


@app.route('/login')
def login_form():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username and password and username in users and users[username] == password:
        flash("You are successfully logged in")
        session['logged_in'] = True
        return redirect(url_for('account'))

    message = "Wrong username/password"
    return render_template('login.html', message=message)


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


@app.route('/logout')
def logout():
    if not session.get('logged_in'):
        return "Not logged in"
    else:
        session['logged_in'] = False
    return render_template('logout.html')


@app.route('/register')
def register():
    return render_template('register.html')


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
