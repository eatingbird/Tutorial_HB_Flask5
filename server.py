from flask import Flask, request, render_template, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
import jinja2

from positions import job_titles

app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index():
    """Loads homepage index.html"""

    return render_template("index.html")

@app.route("/application-form")
def form():
    """Show application form. Get the input by POST.
    Data from application-form.html to /application-form"""

    return render_template("application-form.html",
                           job_titles=job_titles)


@app.route("/application-success", methods=["POST"])
def show_post():
    """ Post data through application-form.html <form action> 
    to application-response.html"""
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    salary = request.form.get('salary')
    job_title = request.form.get('job_title')

    # If salary is a float, limit the decimal places to two.
    salary = float(salary)
    if int(salary) == float(salary):
        salary = int(salary)
    else:
        salary = round(float(salary), 2)
    
    # Add number formating to the salary (thousand separator and dollar)
    salary = "${:,}".format(salary)
    
    return render_template('application-response.html',
                           first_name=first_name, last_name=last_name,
                           salary=salary, job_title=job_title)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
