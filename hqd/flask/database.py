import pymysql
import re


class Database:
    def __init__(self):
        # MySQL
        host = 'localhost'
        user = 'root'
        password = 'rootroot'
        db = 'PythonDB'
        self.conn = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def list_employees(self):
        self.cursor.execute("SELECT * FROM Employees")
        result = self.cursor.fetchall()
        return result

    def list_users(self):
        self.cursor.execute("SELECT * FROM Users")
        result = self.cursor.fetchall()
        return result

    def fetch_user(self, id, user_name):
        self.cursor.execute("SELECT * FROM Users WHERE id = %s AND user = %s", (id, user_name))
        result = self.cursor.fetchone()
        return result

    def verify_user(self, user_name, password):
        self.cursor.execute("SELECT * FROM Users WHERE user = %s AND password = %s", (user_name, password))
        user = self.cursor.fetchone()
        if user is not None:
            return user['id']
        return 0

    def add_user(self, username, password, email):
        self.cursor.execute('SELECT * FROM Users WHERE user = %s', username)
        account = self.cursor.fetchone()

        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            self.cursor.execute('INSERT INTO Users VALUES (NULL, %s, %s, %s)', (username, password, email))
            self.conn.commit()
            msg = 'You have successfully registered!'
        return msg
