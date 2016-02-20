from flask import Flask
from flask import render_template

app = Flask("MyApp")


@app.route("/")
def hello():
	return render_template("hello.html")

# just checking

@app.route("/<name>")
def hello_someone(name):
	return render_template("hello.html", name=name.title())

app.run()