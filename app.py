import sys
import flask
from flask import Flask
from insurance.logger import logging
from insurance.exception import insuranceException
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    try:
        pass
        #raise Exception("we are testing custom exception")
    except Exception as e:
        insurance = insuranceException(e,sys)
        logging.info(insurance.error_message)
        logging.info("we are testing logging module")
    return "Starting internship Project with CI/CD pipeline"

if __name__=="__main__":
    app.run(debug=True)

