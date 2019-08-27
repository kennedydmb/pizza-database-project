import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'pizza_manager'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

mongo = PyMongo(app)

# Make local dictionaries for database values
meats = mongo.db.ingredients.find_one({'meats' : {'$exists': True}})
vegs = mongo.db.ingredients.find_one({'vegs' : {'$exists': True}})
sauces = mongo.db.sauces.find_one({'sauces' : {'$exists': True}})
cheeses = mongo.db.cheeses.find_one({'cheeses' : {'$exists': True}})
ingredients = mongo.db.ingredients.find()
users = mongo.db.users

                            
@app.route('/')
# Route for pizzas.html, local dicts passed through. This page displays pizzas 
# currently in the system.
@app.route('/get_pizzas')
def get_pizzas():
    return render_template("pizzas.html",
    pizzas=mongo.db.pizzas.find(), 
    meats = mongo.db.ingredients.find_one({'meats' : {'$exists': True}}),
    vegs = mongo.db.ingredients.find_one({'vegs' : {'$exists': True}}),
    sauces = mongo.db.sauces.find_one({'sauces' : {'$exists': True}}),
    cheeses = mongo.db.cheeses.find_one({'cheeses' : {'$exists': True}}))

# Route for adding new pizzas to the database. Local dicts passed though.
# User can choose pizza ingredients and add aadditional notes here.
@app.route('/add_pizza')
def add_pizza():
    return render_template("addpizza.html", 
    meats = mongo.db.ingredients.find_one({'meats' : {'$exists': True}}),
    vegs = mongo.db.ingredients.find_one({'vegs' : {'$exists': True}}),
    sauces = mongo.db.sauces.find_one({'sauces' : {'$exists': True}}),
    cheeses = mongo.db.cheeses.find_one({'cheeses' : {'$exists': True}}))
                         
# Route for posting form created in addpizza.html                           
@app.route('/insert_pizza', methods=['POST'])
def insert_pizza():
    pizzas=mongo.db.pizzas
    complex = {
	'pizza_name' : request.form.get('pizza_name'),
	'pizza_code' : request.form.get('pizza_code'),
	'sauce_type' : request.form.get('sauce_type'),
	'cheese_type' : request.form.get('cheese_type'),
	'pizza_notes' : request.form.get('pizza_notes'),
	# So you can build your data struture
	# as you wish but also make it as complex as you need it
	'toppings' : request.form.getlist('toppings'), # This would embed an array into your dict..
}
    mongo.db.pizzas.insert_one(complex)
    return redirect(url_for('get_pizzas'))



@app.route('/get_toppings')
def get_toppings():
    return render_template('toppings.html',
                           meats = meats,
                           vegs = vegs)

@app.route('/add_topping')
def add_topping():
    return render_template('addtopping.html',
    meats = meats,
    vegs = vegs)


@app.route('/add_meat')
def add_meat():
    return render_template("addmeat.html", 
                           meats = meats)
                           
@app.route('/insert_meat_topping/<meat_id>', methods=['POST'])
def insert_meat_topping(meat_id):
    mongo.db.ingredients.update(
        {'_id': ObjectId(meat_id)},
        {'$addToSet':{'meats' : request.form.get('meats')}},
        upsert=True)
    return redirect(url_for('get_pizzas'))
    
@app.route('/add_veg')
def add_veg():
    return render_template("addveg.html", 
                           vegs = vegs)
                           
@app.route('/insert_veg_topping/<veg_id>', methods=['POST'])
def insert_veg_topping(veg_id):
    mongo.db.ingredients.update(
        {'_id': ObjectId(veg_id)},
        {'$addToSet':{'vegs' : request.form.get('vegs')}},
        upsert=True)
    return redirect(url_for('get_pizzas'))
                        
@app.route('/edit_pizza/<pizza_id>')
def edit_pizza(pizza_id):
    the_pizza =  mongo.db.pizzas.find_one({"_id": ObjectId(pizza_id)})
    return render_template('editpizza.html', 
                            pizza = the_pizza,
                            sauces = sauces,
                            cheeses=cheeses,
                            meats = meats,
                            vegs = vegs)

@app.route('/update_pizza/<pizza_id>', methods=["POST"])
def update_pizza(pizza_id):
    pizzas = mongo.db.pizzas
    pizzas.update( {'_id': ObjectId(pizza_id)},
    {
        'pizza_name' : request.form.get('pizza_name'),
	    'pizza_code' : request.form.get('pizza_code'),
    	'sauce_type' : request.form.get('sauce_type'),
	    'cheese_type' : request.form.get('cheese_type'),
	    'pizza_notes' : request.form.get('pizza_notes'),
	    'toppings' : request.form.getlist('toppings')}
	    )
    return redirect(url_for('get_pizzas'))

@app.route('/delete_task/<pizza_id>')
def delete_pizza(pizza_id):
    mongo.db.pizzas.remove({'_id': ObjectId(pizza_id)})
    return redirect(url_for('get_pizzas'))

# Taken and modified from Miroslav Svec's (username Miro) sessions from Slack DCD channel
# Login - taken and modified from Miroslav Svec's (username Miro) sessions from Slack DCD channel
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Logs the user into the website. 
    """

    # Check if user is not logged in already
    if 'user' in session:
        user_in_db = users.find_one({"username": session['user']})
        if user_in_db:
            # If so redirect user to their "My Favourites" page
            flash("You are logged in already!")
            return redirect(url_for('get_pizzas'))
    else:
        # Render the page for user to be able to log in
        return render_template("login.html")
        
@app.route('/user_auth', methods=['GET','POST'])
def user_auth():
    """
    Checks user login details from login form
    """
    
    form = request.form.to_dict()
    user_in_db = users.find_one({"username": form['username']})
    # Check for user in database
    if user_in_db:
        # If passwords match (hashed / real password)
        if check_password_hash(user_in_db['password'], form['user_password']):
            # Log user in (add to session)
            session['user'] = form['username']
            return redirect(url_for('get_pizzas'))
        else:
            flash("Wrong password or user name!")
            return redirect(url_for('login'))
    else:
        flash("You must be registered!")
        return redirect(url_for('register'))


# Sign up - taken and modified from Miroslav Svec's (username Miro) sessions from Slack DCD channel
@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Registers new users to the website.
    """
    
    # Check if user is not logged in already
    if 'user' in session:
        flash('You are already signed in!')
        return redirect(url_for('get_pizzas'))
    if request.method == 'POST':
        form = request.form.to_dict()
        # Check if the password and password1 actually match
        if form['user_password'] == form['user_password1']:
            # If so try to find the user in db
            user = users.find_one({"username": form['username']})
            if user:
                flash("That username already exists!")
                return redirect(url_for('register'))
            # If user does not exist register new user
            else:
                # Hash password
                hash_pass = generate_password_hash(form['user_password'])
                # Create new user with hashed password
                users.insert_one(
                    {
                        'username': form['username'],
                        'email': form['email'],
                        'password': hash_pass,
                        'pizzas_created': []
                    }
                )
                # Check if user is actually saved
                user_in_db = users.find_one(
                    {"username": form['username']})
                if user_in_db:
                    # Log user in (add to session)
                    session['user'] = user_in_db['username']
                    return redirect(url_for('get_pizzas'))
                else:
                    flash("There was a problem saving your profile")
                    return redirect(url_for('register'))

        else:
            flash("Passwords dont match!")
            return redirect(url_for('register'))

    return render_template("register.html")

# Log out- taken and modified from Miroslav Svec's (username Miro) sessions from Slack DCD channel
@app.route('/logout')
def logout():
    """
    Logs the users out of the session
    """
    
    
    # Clear the session
    session.clear()
    flash('You have been logged out!')
    return redirect(url_for('get_pizzas'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)