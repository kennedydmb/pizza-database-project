import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'pizza_manager'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

# Make local dictionaries for database values
meats = mongo.db.ingredients.find_one({'meats' : {'$exists': True}})
vegs = mongo.db.ingredients.find_one({'vegs' : {'$exists': True}})
sauces = mongo.db.ingredients.find_one({'sauces' : {'$exists': True}})
cheeses = mongo.db.ingredients.find_one({'cheeses' : {'$exists': True}})
                            
@app.route('/')
# Route for pizzas.html, local dicts passed through. This page displays pizzas 
# currently in the system.
@app.route('/get_pizzas')
def get_pizzas():
    return render_template("pizzas.html",
                           pizzas=mongo.db.pizzas.find(), 
                           meats = meats,
                           vegs = vegs,
                           sauces = sauces,
                           cheeses = cheeses)

# Route for adding new pizzas to the database. Local dicts passed though.
# User can choose pizza ingredients and add aadditional notes here.
@app.route('/add_pizza')
def add_pizza():
    return render_template("addpizza.html", 
                           meats = meats,
                           vegs = vegs,
                           sauces = sauces,
                           cheeses = cheeses)
                         
# Route for posting form created in addpizza.html                           
@app.route('/insert_pizza', methods=['POST'])
def insert_pizza():
    pizzas=mongo.db.pizzas
    complex = {
	'pizza_name' : request.form.get('pizza_name'),
	'pizza_code' : request.form.get('pizza_code'),
	'sauce_type' : request.form.get('sauce_type'),
	'cheese_type' : request.form.get('cheese_type'),
	# So you can build your data struture
	# as you wish but also make it as complex as you need it
	'toppings' : request.form.getlist('toppings'), # This would embed an array into your dict..
}
    mongo.db.pizzas.insert_one(complex)
    return redirect(url_for('get_pizzas'))

@app.route('/add_topping')
def add_topping():
    return render_template('addtopping.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)