from flask import Flask


app=Flask(__name__)

@app.route("/members")
def members():
    return "WELCOME ALL THE MEMBERS  HERE"

@app.route("/")
def welcome():
    return "WELCOME TO THIS PAGE"


if __name__=='__main__':
    app.run()

