from flask import Flask, render_template

app = Flask(__main__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return "smth"



if __name__=="__main__":
    app.run()




