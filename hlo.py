from flask import Flask,render_template
app=Flask(__name__)
@app.route("/<string:name>")
def func(name):
    return render_template("about.html",name=name)
app.run()