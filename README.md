
Cleopatra
=========

Cleopatra allows you to easily produce nicely formatted PDF from .md or .rst files.

  - Type some Markdown text in the left window
  - See the HTML in the right
  - Magic

Markdown is a lightweight markup language based on the formatting conventions that people naturally use in email.  As [John Gruber] writes on the [Markdown site] [1]:

> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually* written in Markdown! To get a feel for Markdown's syntax, type some text into the left window and watch the results in the right.

Version
----

2.0

Tech
-----------

Cleopatra uses a number of open source projects to work properly:

* [Ace Editor] - awesome web-based text editor
* [Marked] - a super fast port of Markdown to JavaScript
* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [node.js] - evented I/O for the backend
* [Express] - fast node.js network app framework [@tjholowaychuk]
* [keymaster.js] - awesome keyboard handler lib by [@thomasfuchs]
* [jQuery] - duh
* [dillinger]
* [wkhtmltopdf]

Installation
--------------

```sh
git clone [git-repo-url] cleopatra
cd cleopatra
npm i -d
mkdir -p public/files/{md,html,pdf}
```

##### Configure Plugins. Instructions in following README.md files

* plugins/googledrive/README.md

```sh
node app
```

For Nodejitsu Deployment
----------

```sh
npm version [ | major | minor | patch | build]
jitsu deploy
```


License
----

MIT

*Free Software, Hell Yeah!*

  [john gruber]: http://daringfireball.net/
  [@thomasfuchs]: http://twitter.com/thomasfuchs
  [1]: http://daringfireball.net/projects/markdown/
  [Marked]: https://github.com/chjj/marked
  [ace editor]: http://ace.ajax.org
  [node.js]: http://nodejs.org
  [Twitter Bootstrap]: http://twitter.github.com/bootstrap/
  [keymaster.js]: https://github.com/madrobby/keymaster
  [jQuery]: http://jquery.com
  [@tjholowaychuk]: http://twitter.com/tjholowaychuk
  [express]: http://expressjs.com
  [wkhtmltopdf]: https://code.google.com/p/wkhtmltopdf/
  [dillinger]: https://github.com/joemccann/dillinger

=======
![image](http://dreamsofpy.github.io/assets/img/slider/slider3.jpg)



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
* **Back-End:**
    * Set up the models for user registration, login/logout, etc
    * Decide which libraries are needed to convert MD2PDF
* **Front-End:**
    * Create a template for the final pdf output
    * Survey forms for each person to fill out
* **Dev/Ops or QA:**
    * Find web hosting for staging a version
    * Set up testing strategy

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

1. If you are using the vagrant set-up from [here](https://github.com/DreamsofPy/vagrant-setup) you
should ssh into the vagrant box and go to the '/vagrant' folder. If you are not using vagrant skip to (2).

         $ cd /vagrant
         $ git clone git@github.com:DreamsofPy/The_Resume_App.git
         $ cd The_Resume_App

2. Clone the repo.

        $ git clone git@github.com:DreamsofPy/The_Resume_App.git
        $ cd The_Resume_App

3. Initialize and activate a virtualenv:

        $ virtualenv --no-site-packages env
        $ source env/bin/activate

4. Install the dependencies:

        $ pip install -r requirements.txt

5. Run the development server:

        $ python app.py

6. Navigate to [http://localhost:5000](http://localhost:5000)

Learn More
---------

* [mkd2pdf](https://github.com/jdodds/mkd2pdf)
* [flask boilerplate](https://github.com/DreamsofPy/flask-boilerplate)
