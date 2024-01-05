# Develop a Flask app that uses URL parameters to display dynamic content.

from flask import Flask , render_template , request

app = Flask(__name__)

@app.route('/')

def homepage():
    return render_template('index.html')

@app.route('/login',methods =['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form('username')
        password = request.form('password')

    return render_template('login.html')


if __name__ == '__main__':
    app.run()
