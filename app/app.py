from crypt import methods
from urllib import request
from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql
import pymysql

# connecting to the database
connection = pymysql.connect (host="localhost", user="root", password="123", database="colyser")

# setting the cursor
cursor = connection.cursor()

app = Flask(__name__)

app.config.update (
    TEMPLATES_AUTO_RELAOD = True
)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route("/newcase", methods=["GET", "POST"])
def newcase():
    
    totalcount = cursor.execute("SELECT * FROM user_table;")
    mencount = cursor.execute("SELECT * FROM user_table where gender = 'M';")
    womencount = cursor.execute("SELECT * FROM user_table where gender = 'F';")
    othercount = cursor.execute("SELECT * FROM user_table where gender = 'O';")
    coughcount = cursor.execute("SELECT * FROM user_table where cough = 'yes';")
    fevercount = cursor.execute("SELECT * FROM user_table where fever = 'yes';")
    breathcount = cursor.execute("SELECT * FROM user_table where breath = 'yes';")
    fatiguecount = cursor.execute("SELECT * FROM user_table where fatigue = 'yes';")
    bodyachecount = cursor.execute("SELECT * FROM user_table where bodyache = 'yes';")
    headachecount = cursor.execute("SELECT * FROM user_table where headache = 'yes';")
    throatcount = cursor.execute("SELECT * FROM user_table where throat = 'yes';")
    runnynosecount = cursor.execute("SELECT * FROM user_table where runnynose = 'yes';")
    nauseacount = cursor.execute("SELECT * FROM user_table where nausea = 'yes';")
    
    connection.commit()
    
    if request.method == "GET":
        return render_template("index.html", totalcount=totalcount, mencount=mencount, womencount=womencount, othercount=othercount, coughcount=coughcount, fevercount=fevercount, breathcount=breathcount, fatiguecount=fatiguecount, bodyachecount=bodyachecount, headachecount=headachecount, throatcount=throatcount, runnynosecount=runnynosecount, nauseacount=nauseacount)
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
            
            return render_template("index.html", totalcount=totalcount, mencount=mencount, womencount=womencount, othercount=othercount, coughcount=coughcount, fevercount=fevercount, breathcount=breathcount, fatiguecount=fatiguecount, bodyachecount=bodyachecount, headachecount=headachecount, throatcount=throatcount, runnynosecount=runnynosecount, nauseacount=nauseacount)
            
        except connection.Error as err:
            return render_template("dberror.html", totalcount=totalcount, mencount=mencount, womencount=womencount, othercount=othercount, coughcount=coughcount, fevercount=fevercount, breathcount=breathcount, fatiguecount=fatiguecount, bodyachecount=bodyachecount, headachecount=headachecount, throatcount=throatcount, runnynosecount=runnynosecount, nauseacount=nauseacount)
        
if __name__ == "__main__":
    app.run()
