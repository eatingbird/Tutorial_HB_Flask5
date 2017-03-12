from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import jinja2

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

    return render_template("application-form.html")


@app.route("/application-success", methods=["POST"])
def show_post():
    """ Post data through application-form.html <form action> 
    to application-response.html"""
    first = request.form.get('first')
    last = request.form.get('last')
    salary = request.form.get('salary')
    job = request.form.get('job')


    # If salary is a float, limit the decimal places to two.
    salary = float(salary)
    if int(salary) == float(salary):
        salary = int(salary)
    else:
        salary = round(float(salary), 2)
    
    # Add number formating to the salary (thousand separator and dollar)
    salary = "${:,}".format(salary)

    return render_template('application-response.html',
                           first=first, last=last,
                           salary=salary, job=job)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
