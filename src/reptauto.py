#
# reptauto.py
# Authors:
#   Samuel Vargas
#

import uuid
from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name__)
app.config["SECRET_KEY"] = str(uuid.uuid4())

USERNAME = "asu"
PASSWORD = "asu"  # Change this to whatever


#
# Server Routes
#

@app.errorhandler(404)
def oops(*args):
    return redirect(url_for('dashboard'))

@app.route('/login')
def login():
    if 'authenticated' in session:
        return redirect(url_for('dashboard'))
    return render_template("login.html")


@app.route('/logout')
def logout():
    if 'authenticated' in session:
        session.pop('authenticated')
    return redirect(url_for('login'))


@app.route('/')
def index():
    if 'authenticated' not in session:
        return redirect(url_for('login'))
    return redirect(url_for("dashboard"))


@app.route('/dashboard')
def dashboard():
    if 'authenticated' not in session:
        return redirect(url_for('login'))
    return render_template("dashboard.html")


#
# Server API
#

@app.route('/api/login', methods=["POST"])
def login_api():
    content = request.get_json(silent=True, force=True)
    if content is None:
        return "Missing {'username': xyz, 'password': 'abc}", 400

    if content['username'] == USERNAME and \
            content['password'] == PASSWORD:
        session['authenticated'] = True
        return "OK", 200

    return "Bad password or username", 403


if __name__ == '__main__':
    app.run(debug=True)
