from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
def primeira_pagina():
    name = "Hector"
    return render_template("index.html", index_variable=name)

@app.route("/sobre-flask")
def sobre_flask():
    return render_template("sobre_flask.html")

if __name__ == "__main__":
    app.run(debug=True)
