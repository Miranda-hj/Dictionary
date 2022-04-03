from flask import Flask, render_template,request,jsonify


app = Flask(__name__)

@app.route("/")
def Dictionary():
    return render_template("app.html")

if __name__ == '__main__':
    Flask.run(app,debug=True)