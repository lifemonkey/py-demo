from flask import *

app = Flask(__name__, template_folder='templates')
app.secret_key = 'test secret key'

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


@app.route("/account")
def account():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    return render_template('account.html')


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
