from database import db, Puppy

# Note lots of ORM filter options here.
# filter(), filter_by(), limit(), order_by(), group_by()
# Also lots of executor options
# all(), first(), get(), count(), paginate()

all_puppies = Puppy.query.all()  # list of all puppies in table
print(all_puppies)
print('\n')

# # Grab by id
# puppy_one = Puppy.query.get(1)
# print(puppy_one)
# print(puppy_one.age)
# print('\n')

# # Filters
# puppy_sam = Puppy.query.filter(Puppy.age > 3).all()  # Returns list
# print(puppy_sam)
# print('\n')
