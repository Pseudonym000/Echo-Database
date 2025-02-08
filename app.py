from flask import Flask, render_template

app = Flask(__name__, static_folder="static")

@app.route('/')
def index():
    return render_template('newsfeed.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/page')
def post():
    return render_template('post.html')

if __name__ == '__main__':
    app.run(debug=True)
