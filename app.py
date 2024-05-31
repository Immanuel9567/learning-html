from flask import Flask, render_template

app = Flask(" - v8's website - ")
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/gallery")
def gallery_page():
    return render_template("gallery.html")

@app.route("/mydevices")
def devices_page():
    return render_template("mydevices.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
