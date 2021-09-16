from flask import Flask, render_template
from utils.scraper import scrapped

app = Flask(__name__)

@app.route("/")
@app.route("/<path:url>")
def root(url=None):
    value = url
    if value:
        return scrapped(value)
    else:
        return "Hello world"

# @app.route("/form", methods=["POST","GET"])
# def form():
#     return render_template("form.html")

# @app.route("/form_submit", methods=["POST", "GET"])
# def submitted():
#     return "It's submitted"

if __name__ == "__main__":
    app.run(debug=True)
