from flask import render_template, request
from database import db, app
from models import Puppy


@app.route("/")
def home(puppy_name=None):
    return render_template('home.html', puppy_name=puppy_name)


@app.route("/puppies/new")
def new():
    return render_template('puppies/new.html')


@app.route("/puppies", methods=["POST"])
def create():
    name = request.form.get('name')
    age = request.form.get('age')
    breed = request.form.get('breed')

    new_puppy = Puppy(name, age, breed)
    db.session.add(new_puppy)
    db.session.commit()

    # Implement your code to create a new Puppy object and then save it to DB.

    return home(new_puppy.name)


@app.route("/puppies/index", methods=["GET"])
def index():
    puppies = Puppy.query.all()
    return render_template('puppies/index.html', puppies=puppies)


@app.route("/puppies/<id>", methods=["GET"])
def show(id):
    puppy = Puppy.query.get(id)
    return render_template('puppies/show.html', puppy=puppy)


@app.route("/puppies/<id>/edit", methods=["GET"])
def edit(id):
    puppy = Puppy.query.get(id)
    return render_template('puppies/edit.html', puppy=puppy)


@app.route("/puppies/<id>", methods=["POST"])
def update(id):
    editted_puppy = Puppy.query.get(id)
    editted_puppy.name = request.form.get('name')
    editted_puppy.age = request.form.get('age')
    editted_puppy.breed = request.form.get('breed')
    db.session.add(editted_puppy)
    db.session.commit()
    return home(editted_puppy.name)


@app.route("/puppies/<pup_id>/drop", methods=["POST"])
def destroy(pup_id):
    pup = Puppy.query.get(pup_id)
    db.session.delete(pup)
    db.session.commit()


if __name__ == '__main__':
    app.run()
