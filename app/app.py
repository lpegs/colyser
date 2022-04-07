from crypt import methods
from urllib import request
from flask import Flask, render_template, request
import sqlite3 as sql
import pymysql

# connecting to the database
connection = pymysql.connect (host="localhost", user="root", password="123", database="colyser")

# setting the cursor
cursor = connection.cursor()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route("/newcase", methods=["GET", "POST"])
def newcase():
    if request.method == "GET":
        return render_template("index.html")
    else:

        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]
        cough = request.form["cough"]
        fever = request.form["fever"]
        breath = request.form["breath"]
        fatigue = request.form["fatigue"]
        bodyache = request.form["bodyache"]
        headache = request.form["headache"]
        throat = request.form["throat"]
        runnynose = request.form["runnynose"]
        nausea = request.form["nausea"]
        
        try:           
            sql = "INSERT INTO user_table (name, age, gender, cough, fever, breath, fatigue, bodyache, headache, throat, runnynose, nausea) VALUES ('" + name + "', '" + age + "', '" + gender + "', '" + cough + "', '" + fever + "', '" + breath + "', '" + fatigue + "', '" + bodyache + "', '" + headache + "', '" + throat + "', '" + runnynose + "', '" + nausea + "')"
            cursor.execute(sql)
            connection.commit()
            
            return render_template("successfull.html")
            
        except connection.Error as err:
            return render_template("dberror.html", name=name)
        
if __name__ == "__main__":
    app.run()
