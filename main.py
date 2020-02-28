from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route('/resume')
def download_resume():
	path = "templates/CV_LAMV_Duke_16022020.pdf"
	return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
