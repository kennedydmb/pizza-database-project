import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'pizza_manager'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

meats = mongo.db.ingredients.find_one({'meats' : {'$exists': True}})
vegs = mongo.db.ingredients.find_one({'vegs' : {'$exists': True}})
sauces = mongo.db.ingredients.find_one({'sauces' : {'$exists': True}})
cheeses = mongo.db.ingredients.find_one({'cheeses' : {'$exists': True}})
                            
@app.route('/')
@app.route('/get_pizzas')
def get_pizzas():
    return render_template("pizzas.html",
                           pizzas=mongo.db.pizzas.find(), 
                           meats = meats,
                           vegs = vegs,
                           sauces = sauces,
                           cheeses = cheeses)

@app.route('/add_pizza')
def add_pizza():
    return render_template("addpizza.html", 
                           meats = meats,
                           vegs = vegs,
                           sauces = sauces,
                           cheeses = cheeses)
                           
@app.route('/insert_pizza', methods=['POST'])
def insert_pizza():
    pizzas =  mongo.db.pizzas
    pizzas.insert_one(request.form.to_dict())
    return redirect(url_for('get_pizzas'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)