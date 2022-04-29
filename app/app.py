from flask import Flask, render_template 
import pandas as pd
# from sqlalchemy import create_engine
# from sqlalchemy.engine import URL
import os 



# df = pd.read_csv("anaemia.csv")
# data = df.to_json(orient='records')

# create app 
app = Flask(__name__)



# page routes

@app.route("/")
def index():
    return render_template("index.html")

    
@app.route("/dashboard_c.html")
def dashboard_c():
    return render_template("dashboard_c.html")

    
@app.route("/forecast_c.html")
def forecast_c():
    return render_template("forecast_c.html")

@app.route("/dashboard_w.html")
def dashboard_w():
    return render_template("dashboard_w.html")

@app.route("/forecast_w.html")
def forecast_w():
    return render_template("forecast_w.html")

# the below apis need to be thought out more...since the addition of children in the project. - for the moment the below links are inactive.
@app.route("/api/data")
def data():
    df = pd.read_csv("https://anaemia-app-bucket-01.s3.ap-southeast-2.amazonaws.com/anaemia_women.csv")
    data = df.to_dict(orient = 'records')
    return {'data':data}


@app.route("/api/predict")
def predict():
    df = pd.read_csv("https://anaemia-app-bucket-01.s3.ap-southeast-2.amazonaws.com/anaemia_women_forecast.csv")
    data = df.to_dict(orient = 'records')
    return {'data':data}





if __name__ == "__main__":
    app.run(debug=True)
