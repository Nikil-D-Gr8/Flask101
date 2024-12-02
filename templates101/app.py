from flask import Flask, render_template
app = Flask(__name__)

# sample posts for us to just loop over
posts = [
    {
        'author' :'Nikil',
        'title' : 'Nikil Blog',
        'content': 'This is just a random post',
        'date' : 'April 21, 2024'
    }
    ,
    {
        'author' :'Paul',
        'title' : 'Paul Blog',
        'content': 'This is a post',
        'date' : 'April 11, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",posts=posts)
# we use render template function to render a webpage 
# we can also pass some information with it to the webpage

@app.route("/about")
def about():
    return render_template("about.html",title="Nikil")


if __name__ == "__main__":
    app.run(debug=True)

