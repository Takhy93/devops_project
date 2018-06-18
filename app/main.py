#!/usr/bin/python3
from flask import Flask
from flask import render_template
# instancie une app
app = Flask(__name__)
# in debug mode :P
app.debug = True
# secret key contre csrf
app.secret_key = "secret"
@app.route("/")
def index():
    return "hello"
def root_page(one_id):
    txt = render_template("index.html", page_id=one_id)
    return txt

if __name__ == "__main__":
    # forever serve
    app.run(debug=True)
