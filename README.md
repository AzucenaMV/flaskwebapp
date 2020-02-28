# flaskwebapp
This a website app created with Flask in Google Cloud Platform. The README file contains all the instructions to build it from scratch or you can also copy the docker image.

I recently learned how to start using Flask and deploying in a Cloud environment. This time I want to add one more step: Docker containers. 

This tutorial is a step by step guide for building the website app. It assumes that you already have an account in GCP.

Create a new project



Provide a name for your project


Make sure you are working your newly created project: 


Click on activate cloud shell

Accept the terms

Create and activate a virtualenv to test your app locally

```
>>virtualenv ./.flaskwebapp
>>source ./.flaskwebapp/bin/activate
```

Click on launch editor



Create a new folder for your project


Create a main.py file

```
>>nano main.py
```

Paste:
```
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
```

It should look like this: 


Create a requirements file
```
>>nano requirements.txt
```
Add:
```
flask==1.1.1
```

Create a makefile 
```
>>nano makefile
```

Paste:
```
install:
    pip install --upgrade pip &&\
        pip install -r requirements.txt
 
lint:
    pylint --disable=R,C main.py
 
all: install lint test
```

Create a templates dir and a static/css dir 
```
>>mkdir templates
>>mkdir static
>>cd static
>>mkdir css
```
Inside templates create the html files that will need
```
>> nano home.html
```

Paste :

```
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Web App Using Flask</title>
  </head>
  <body>
    {% extends "layout.html" %}
    {% block content %}
    <div class = "home">
    <h1> Web App Using Flask </h1>
    <h4> Welcome! </h4>
    <p> I created this portfolio website using Flask and Google Cloud Platform. <br>If you want
        to learn how to create it please see this repo in github or you can copy the Docker image.</p>
    </div>
    {% endblock %}
  </body>
</html>
```

```
>> nano about.html
```

Paste :

```
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>About Flask</title>
  </head>
  <body>
    {% extends "layout.html" %}
    {% block content %}
       <div class="about">
         <h1>About me</h1>
         <p>My name is Azucena Morales. I'm a second year Data Science Master student at Duke University</p>
       </div>
     {% endblock %}
  </body>
</html>
```


```
>> nano projects.html
```

Paste :

```
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>About Flask</title>
  </head>
  <body>
    {% extends "layout.html" %}
    {% block content %}
  <!-- First Photo Grid-->
<div class="row">
  <div class="column">
    <div class="content">
      <!--<img src="/w3images/sandwich.jpg" alt="Sandwich" style="width:100%">-->
      <h3>Project A</h3>
      <p>Description about project A</p>
    </div>
  </div>
  <div class="column">
    <div class="content">
      <h3>Project B</h3>
      <p>Description about project B</p>
    </div>
  </div>
  <div class="column">
    <div class="content">
      <h3>Project C</h3>
      <p>Description about project C</p>
    </div>
  </div>
        {% endblock %}
   </div>
```

Our html files will inherit from this file
```
>> nano layout.html
```

Paste :

```
 <!DOCTYPE html>
    <!DOCTYPE html>
    <html>
      <head>
        <title>Flask app</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/main7.css') }}">
      </head>
      <body>
        <header>
        <div class="container">
            <h1 class="logo">Azucena MV</h1>
            <strong><nav>
            <ul class="menu">
                <li><a href="{{ url_for('home') }}">Home</a></li>
                <li><a href="{{ url_for('about') }}">About</a></li>
                <li><a href="{{ url_for('projects') }}">Projects</a></li>
                <li><a href="{{ url_for('.download_resume') }}">Resume</a></li>
            </ul>
            </nav></strong>
        </div>
        </header>
        <div class="container">
          {% block content %}
          {% endblock %}
        </div>
      </body>
    </html>
```

Finally the css file:
```
>> nano layout.html
```

Paste :

```
    body {
      margin: 0;
      padding: 0;
      font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
      color: #444;
    }
    /*
     * Formatting the header area
     */
    header {
      background-color: #444;
      height: 50px;
      width: 100%;
      opacity: .9;
      margin-bottom: 10px;
    }
    header h1.logo {
      margin: 0;
      font-size: 1.7em;
      color: #fff;
      float: left;
    }
    header h1.logo:hover {
      color: #fff;
      text-decoration: none;
    }
    /*
     * Centering the body content
     */
    .container {
      width: 1200px;
      margin: 0 auto;
    }
    div.home {
      padding: 10px 0 30px 0;
      -webkit-border-radius: 6px;
         -moz-border-radius: 6px;
              border-radius: 6px;
    }
    div.about {
      padding: 10px 0 30px 0;
      -webkit-border-radius: 6px;
         -moz-border-radius: 6px;
              border-radius: 6px;
    }
    h2 {
      font-size: 3em;
      margin-top: 40px;
      text-align: center;
      letter-spacing: -2px;
    }
    h3 {
      font-size: 1.7em;
      font-weight: 100;
      margin-top: 30px;
      text-align: center;
      letter-spacing: -1px;
      color: #999;
    }
   
   .menu {
        float: right;
        margin-top: 8px;
    }
    .menu li {
        display: inline;
    }
    .menu li + li {
        margin-left: 35px;
    }
    .menu li a {
        color: #fff;
        text-decoration: none;
    }
 
    .menu li a:hover {
        background-color: #555;
        color: white;
    }
 
.active {
  color: gainsboro;
}
 
* {
  box-sizing: border-box;
}
.row {
  margin: 8px -16px;
}
 
/* Add padding BETWEEN each column (if you want) */
.row,
.row > .column {
  padding: 8px;
}
 
/* Content */
.content {
  background-color: whitesmoke;
  padding: 10px;
}
 
/* Create four equal columns that floats next to each other */
.column {
  float: left;
  width: 33%;
}
 
/* Clear floats after rows */
.row:after {
  content: "";
  display: table;
  clear: both;
}
 
/* Responsive layout - makes a two column-layout instead of four columns */
@media screen and (max-width: 900px) {
  .column {
    width: 50%;
  }
}
 
/* Responsive layout - makes the two columns stack on top of each other instead of next to each other */
@media screen and (max-width: 600px) {
  .column {
    width: 100%;
  }
}
```

The structure of your directory should look similar to this



Make sure you are inside your virtualenv and test it!
```
>>python3 main.py
```
If all is working fine, you should be able to run the website app in http://0.0.0.0:8080/

You are free to work with this now! 

Let’s create the dockerfile 
```
>> nano dockerfile
```
paste:
```
FROM python:3.7.3-stretch
 
# Working Directory
WORKDIR /app
 
# Copy source code to working directory
COPY . main.py /app/
 
# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt
 
# Expose port 8080
EXPOSE 8080
 
# Run app.py at container laun.menu
CMD ["python", "main.py"]
```
One last step, upload your resume file to the templates directory.
In main.py change the following line by the name of your file

path = "templates/CV_LAMV_Duke_16022020.pdf"

That’s it!

>>gcloud builds submit --tag gcr.io/PROJECT-ID/helloworld


Skip this part:
#Build the image and don’t forget the dot!
#>>docker build --tag flaskwebapp .
#It should look like this


This will run the image as a container:
>>do
--allow tcp:80


This content was adapted from the following sites:

https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env
https://www.w3schools.com/howto/howto_css_portfolio_gallery.asp
https://pythonhow.com/add-css-to-flask-website/

