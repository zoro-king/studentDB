from application import app
from flask import render_template,flash,request,redirect,url_for
from .forms import StudentForm
from application import db
from bson import ObjectId

@app.route('/')
def get_studb():
    student=[] 
    for stud in db.stud_flask.find().sort("name"):
        stud["_id"] = str(stud["_id"])
        student.append(stud)
    return render_template("view_studentdb.html",student = student)
 
@app.route('/add_db',methods = ['POST','GET'])
def add_db():
    if request.method == "POST":
        form = StudentForm(request.form)
        stud_name=form.name.data
        stud_department=form.department.data
        stud_year=form.year.data

        db.stud_flask.insert_one({
            "name":stud_name,
            "department":stud_department,
            "year":stud_year
        })
        flash("Successfully added","success")
        return redirect("/")
    if request.method == "GET":
        form = StudentForm()
        return render_template("add_studb.html",form = form)


@app.route("/update_stud/<id>",methods=["POST","GET"])
def update_stud(id):
    if request.method == "POST":
        form = StudentForm(request.form)
        stud_name=form.name.data
        stud_department=form.department.data
        stud_year=form.year.data
        db.stud_flask.find_one_and_update({"_id":ObjectId(id)}, {"$set":{
            "name":stud_name,
            "department":stud_department,
            "year":stud_year
        }})

        flash("Student detils successfully update","success")
        return redirect("/")

    else:
        form=StudentForm()
        stud=db.stud_flask.find_one({"_id":ObjectId(id)})
        form.name.data = stud.get("name",None)
        form.department.data = stud.get("department",None)
        form.year.data = stud.get("year",None)

    return render_template("add_studb.html",form=form)


@app.route("/delete_stud/<id>")
def delete_stud(id):
    db.stud_flask.find_one_and_delete({"_id":ObjectId(id)})
    flash("Student record deleted","success")
    return redirect("/")