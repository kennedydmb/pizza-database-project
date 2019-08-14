import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'pizza_manager'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

meat = mongo.db.ingredients.find_one({'meat' : {'$exists': True}})
veg = mongo.db.ingredients.find_one({'veg' : {'$exists': True}})
                    
print(veg)
print(meat)
                            
@app.route('/')
@app.route('/get_pizzas')
def get_pizzas():
    return render_template("pizzas.html",
                           pizzas=mongo.db.pizzas.find(), 
                           meat = meat,
                           veg = veg)
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)