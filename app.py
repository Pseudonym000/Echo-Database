from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def blogpage():
    return render_template('blogpage.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/profile')
def profile():
    return render_template('Profile.html')

@app.route('/blogpost')
def blogpost():
    return render_template('blogpost.html')

if __name__ == '__main__':
    app.run(debug=True)
