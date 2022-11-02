from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<a href=/mis>MIS</a><br>"
    homepage += "<a href=/me>關於我</a><br>"
    return homepage

@app.route("/me")
def me():
    return render_template("aboutme.html")

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

#@app.route("/today")
#def today():
    #now = datetime.now()
   # return render_template("today.html", datetime = str(now))

if __name__ == "__main__":
    app.run()
