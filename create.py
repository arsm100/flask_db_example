from database import db, Puppy

# This is how you create an entry to database
# create an instance of Puppy
my_puppy = Puppy('Jessica', 4, 'German Shepard')
my_puppy1 = Puppy('bobby', 2, 'Pug')
my_puppy2 = Puppy('Porishka', 3, 'Husky')

# save it to database with the following 2 lines of code
db.session.add(my_puppy)
db.session.add(my_puppy1)
db.session.add(my_puppy2)
db.session.commit()
