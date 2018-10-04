from flask import render_template, request
from database import db, app
from models import Puppy

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/puppies/new")
def new():
    return render_template('puppies/new.html')

@app.route("/puppies", methods=["POST"])
def create():
    name = request.form.get('name')
    age = request.form.get('age')
    breed = request.form.get('breed')

    # Implement your code to create a new Puppy object and then save it to DB.

    return "Success" # modify this to redirect to show page after implementing show page

@app.route("/puppies", methods=["GET"])
def index():
    pass

@app.route("/puppies/<id>", methods=["GET"])
def show(id):
    pass

@app.route("/puppies/<id>/edit", methods=["GET"])
def edit(id):
    pass

@app.route("/puppies/<id>", methods=["PUT"])
def update(id):
    pass

@app.route("/puppies/<id>", methods=["DESTROY"])
def destroy(id):
    pass

if __name__ == '__main__':
    app.run()
