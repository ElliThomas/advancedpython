from flask import Flask
from flask import render_template

app = Flask("MyApp")


@app.route("/")
def about():
	return render_template("about.html")

@app.route("/<name>")
def hello_someone(name):
	return render_template ("about.html", name=name.title())

app.run()