from flaskdemo import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    user = { 'name': 'Awesome User' }
    return render_template('index.html', title='Home', user=user)
