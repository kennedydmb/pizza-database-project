import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'pizza_manager'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)



@app.route('/')
@app.route('/get_pizzas')
def get_pizzas():
    ingredients = list(mongo.db.ingredients.find({'topping_type':'veg'}))
    return render_template("pizzas.html",
                           pizzas=mongo.db.pizzas.find(), 
                           ingredients=ingredients)
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)