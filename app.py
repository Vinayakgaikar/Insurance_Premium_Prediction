from distutils.log import debug
import flask
from flask import Flask

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return "Starting inuron internship Project"

if __name__=="__main__":
    app.run(debug=True)

