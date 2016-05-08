"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
brand = Brand.query.get('8')

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
# model = Model.query.filter_by(name='Corvette').all() #queries same results as below
models = Model.query.filter((Model.name == 'Corvette') & (Model.brand_name == 'Chevrolet')).all()

# Get all models that are older than 1960.
models = Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
brands = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
models = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
brands = Brand.query.filter((Brand.founded == 1903) & (Brand.discontinued.is_(None))).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
brands = Brand.query.filter(Brand.discontinued != None).all()
# brands = Brand.query.filter(Brand.founded < 1950).all()

# Get any model whose brand_name is not Chevrolet.
models = Model.query.filter(Model.brand_name != 'Chevrolet').all()


# Fill in the following functions. (See directions for more info.)
def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    # Returns a list of Model objects
    models = db.session.query(Model).filter(Model.year == year).all()

    # for-loop to iterate of the list of object and get a single object out
    for model in models:
        # calls attributes on the single model object from the Model Class
        model_name = model.name
        brand_name = model.brand_name
        #have to call the model object as well as the brand attribute from the brands table
        # in the Brand Class to get the headquarters. Set relationship between both classes to call this attribute.
        headquarters = model.brand.headquarters

    print "Model name: %s \nBrand name: %s \nHeadquarters: %s \n" % (model_name, brand_name, headquarters)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands = db.session.query(Model.brand_name, Model.name).all()

    for brand in brands:
        print "Brand name: %s \nModel name: %s \n" % (brand[0], brand[1])

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

    # The returned value is a
    # query of the brands table of the Brand class
    # where name is 'Ford'
    # Its datatype is an object.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

    # An association table is a table you create
    # only for the purpose of managing a relationship between a many-to-many tables.
    # The association table holds the foreign keys that bridge the tables together creating the relationship between them.
    # Having 2 or more foreign keys makes the table an association table.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass
