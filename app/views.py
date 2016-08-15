from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/GetIn')
def getin():
    return "Get In!"

@app.route('/FindMe/<user>')
def findme(user):
    return user


