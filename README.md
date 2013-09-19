![image](http://dreamsofpy.github.io/assets/img/slider/slider3.jpg)

The_Resume_App
==============

Make it easy to produce nicely formatted PDF from .md or .rst files


**Job Seeker Goal:**
Writes experiences with software development in simple text format. Use of this app will automattically generate resume in good looking PDF format. Similar to functionalities of [Marked](http://markedapp.com/).

Tasks:

* **Architecture:**
    * Content for the resume; sections can include qualifications, quantified levels, responsibilities, technical environment, location, industry
    * Decide how user will enter in markdown content
        * Could be file upload or url upload
        * Could be markdown/preview like http://markable.in/editor/
    * Make it easy to link to social profiles, i.e. github, stack overflow
        * Examples include bitdeli for analyzing your skill level
        * Badges, maybe like coderwall or stack overflow reputation points?
* **Dev/Ops:**
    * Set up files for the app using [flask boilerplate](https://github.com/DreamsofPy/flask-boilerplate)
    * Find web hosting for staging a version
* **Back-End:**
    * Set up the models for user registration, login/logout, etc
* **Front-End:**
    * Create a template for the final pdf output
    * Survey forms for each person to fill out


###This code base uses these python libraries:

**Basic Requirements**

* [Flask](http://flask.pocoo.org/docs/) Web Framework
* Flask-SQlalchemy
* Flask-WTF
* MySQL-python==1.2.4
* Bootstrap
* [Database]() TBD
* [Markdown](https://pypi.python.org/pypi/Markdown)
* [Xhtml2PDF](http://www.xhtml2pdf.com/)


###Project Structure

    ├── Procfile
    ├── Procfile.dev
    ├── app.py
    ├── config.py
    ├── error.log
    ├── forms.py
    ├── models.py
    ├── requirements.txt
    ├── static
    │   ├── css
    │   │   ├── boostrap-responsive.css
    │   │   └── bootstrap.css
    │   ├── img
    │   │   ├── glyphicons-halflings-white.png
    │   │   └── glyphicons-halflings.png
    │   └── js
    │       ├── libs
    │       │   ├── bootstrap.min.js
    │       │   ├── jquery.min.js
    │       │   └── modernizr-2.0.6.min.js
    │       ├── plugins.js
    │       └── script.js
    └── templates
        ├── 404.html
        ├── 500.html
        ├── index.html
        ├── login.html
        ├── register.html
        └── template.html

Quick Start
----------

1. Clone the repo

        $ git clone git@github.com:DreamsofPy/The_Resume_App.git
        $ cd The_Resume_App

2. Initialize and activate a virtualenv:

        $ virtualenv --no-site-packages env
        $ source env/bin/activate

4. Install the dependencies:

        $ pip install -r requirements.txt

5. Run the development server:

        $ python app.py

6. Navigate to [http://localhost:5000](http://localhost:5000)

Learn More
---------

[mkd2pdf](https://github.com/jdodds/mkd2pdf)
[flask boilerplate](https://github.com/DreamsofPy/flask-boilerplate)
