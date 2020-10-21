"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    return render_template("student_info.html",
                            first=first, last=last,
                            github=github)

@app.route("/student_search")
def get_student_form():
    """Show form for searching for a student"""

    return render_template("student_search.html")


@app.route("/student_add")
def student_add():
    """Add a new student form"""

    return render_template("student_add.html")

@app.route("/student_added", methods=['POST'])
def add_student_to_database():
    """Adds new student to database"""

    first = request.form.get('first')
    last = request.form.get('last')
    github = request.form.get('github')

    hackbright.make_new_student(first, last, github)

    first, last, github = hackbright.get_student_by_github(github)

    return render_template("student_added.html", first=first, 
    last=last, github=github)



if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
