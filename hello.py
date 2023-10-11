from flask import Flask
from markupsafe import escape
myapp_obj = Flask(__name__)
@myapp_obj.route("/hello")
def hello():
    return "Hello World!"
@myapp_obj.route("/blueblue")
def blueblue ():
    return "Blueblue"

@myapp_obj.route("/members/<string:name>/)")
def getMember(name):
    return escape(name)
myapp_obj.run()
