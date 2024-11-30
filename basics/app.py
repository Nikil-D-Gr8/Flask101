from flask import Flask
# importing the class
app = Flask(__name__)
# making an object of the class by passing in necessary params

# decorators for route mapping
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/html")
def html():
    return "<h1>Hello World</h1>"