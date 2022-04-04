from email import message
from flask import Flask, render_template,request,jsonify,Response
import mysql.connector
import uuid

app = Flask(__name__)

dbconn = None
cnx = mysql.connector.connect(user="root", host="127.0.0.1",
                                    database="dictionary", password="password",auth_plugin='mysql_native_password'
                                    )
cursor = cnx.cursor()

def genID():
    return uuid.uuid4().fields[1]

@app.route("/")
def Home():
    return Response(render_template("app.html"))

@app.route("/selectLanguage", methods=["POST"])
def selectLanguage():
    phrase=request.form["phrase"]
    language=request.form["language"].lower()
    id="id"+request.form["language"]
    cursor.execute(f"select {language}.translated from english join {language} on english.idEnglish = {language}.{id} where english.english  ='{phrase}';")
    data=cursor.fetchall()
    if data:
        return jsonify({"translated": data})
    else:
        data="Not Recorded"
        return jsonify({"translated": data})

@app.route("/addNew", methods=["POST"])
def addNew():
    phrase=request.form["phrase"]
    translated=request.form["translated"]
    language=request.form["language"].lower()
    print(phrase)
    print(language)
    print(translated)
    id=genID()
    cursor.execute(f"Insert into {language} values({id},'{translated}');")
    cursor.execute(f"Insert into english values({id},'{phrase}');")
    message = "Submitted!"
    return jsonify({"message": message})

if __name__ == '__main__':
    Flask.run(app,debug=True)