from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Home Route</h1>"


# when two decorators are used succesively, they both return the same output
@app.route("/about")
@app.route("/abou")
def about():
    return "<h1>About Route</h1>"


if __name__ == '__main__':
    app.run(debug=True)
# the above runs the app in debug mode
# which essentialy helps us with hot reloading