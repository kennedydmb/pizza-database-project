# Data Centric Development Project

## Milestone Project 3: Pizza Database
### Goal 
To build a full-stack site that allows users to manage a common dataset about pizza recipies.
Users can share thier own data with the community and benefit from having convienient access to data provided by all other members.
Site owner advances their own goals by providing this functioanlity, growing the dataset and by being a user themselves.

An application that implements [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete). 

The application must allow the user to:
- Create new entries in the database.
- View (read) entries in the database.
- Edit existing extries in the database.
- Delete entries in the database.

The idea for this application is that users can check and add to a catalogue of 
pizza recipes. Based off of real world scenario where staff of a pizza shop did
not have access to pizza recipes outside of the work environment as a training aid.

### The application
A single page application that gives an overview pizza recipes. It can show:
- Pizza name
- Pizza code (a 2 character code for quick identifying)
- Sauce type
- Cheese type
- Toppings, meat(red) and veg(green).

[Deployed on Heroku](https://pizza-database.herokuapp.com/)

## UX
![Device Responsiveness Display](https://i.imgur.com/gXQySwf.png "Device displays")

### Users
At this stage the intended users are anyone that would like to view or add to 
the database. Admin functionality is a future feature to implement to give 
greater control to an admin. This would make the app functional for a business to
use with staff members. The app could also be joined with the [previous project.](https://github.com/kennedydmb/Pizza-Efficenciency-Dashboard)

### User Stories.
- As an Operations Director, I want to see how my employees are performing so 
that I can see if our training is effective.
- As a Trainer, I want to see how quickly each member of staff can make pizza 
against how long they have worked for the company. Then I can see clearly who may 
be in need of additional training, and give praise to those working well.
- As a Store Manager, I want to see an overview of my store. Who is the quickest,
who has served the longest, how many employees do I have, what percentage of my
workers are performing to the standard I have set.

### Wireframe
Wireframe can be found [here](https://i.imgur.com/suCL447.jpg?1 "Original Web App Wireframe")

#### Difference To Deployed Version
- Layout of each pizza card remains mostly the same. Pizza code is now sat beside each
pizza name. The toppings are displayed on top of an image and toppings are split side by side.
- Each pizza has an edit button at the bottom of the card.
- Adding a new pizza remains relatively unchanged as well. However pizza code text input is now present.
- The entry fields for name, sauce, code and cheese are all in the same box display.
- Toppings are not switches, but are now checkboxes and split into meat and veg toppings.

#### Data Structure

Cheeses
```
"_id":{"$oid":"5d5c13881c9d440000edb480"},
"cheeses":  "mozzarella",
            "low fat",
            "spicy",
            "none"
```
Ingredients 
```
"_id":{"$oid":"5d5c1e6b160a7224ae45b729"},
"meats":    "bacon",
            "beef",
            "sausage",
            "roast chicken",
            "tandoori chicken",
            "pepperoni",
            "ham",
            "meatballs",
            "chorizo",
            "tuna",
            "catalan chicken",
            "hotdogs",
            "barbacoa beef",
            "spicy beef",
            "chicken tikka"

"_id":{"$oid":"5d5d19cc1c9d4400003fed87"},
"vegs":[...]
            
```
Pizzas
```
"_id":{"$oid":"5d6557e0ff60b8383e44b99f"}
"pizza_name":"Mighty Meaty"
"pizza_code":"MM"
"sauce_type":"pizza"
"cheese_type":"mozzarella"
"pizza_notes":"A meaty pizza originally made by Domino's"
"toppings":"beef","sausage","pepperoni","ham","onions","MUSHROOMS"
"creator":
    "_id":{"$oid":"5d641e9c16b3c94375403520"},"username":"mistarkennedy"
```
Sauces
```
"_id":{"$oid":"5d5c12761c9d440000edb47f"},
"sauces":"pizza","tomato and garlic","bbq","none"
```
Users
```
"_id":{"$oid":"5d6833752b3e364386a94827"},
"username":"AnotherAccount",
"password":"pbkdf2:sha256:150000$CZwihgBS$7133aac8d498f898d75f1ad0b80dc0010a58322955c8068dfde5e9d56a7dfffb",
"pizzas_created":[]
```

### Design
For the color palate I used this [color scheme website](http://colorschemedesigner.com/csd-3.5/)

![Color Scheme](https://i.imgur.com/SCBSKnl.png "Color Scheme")

## Features

### Existing Features

#### Add New Pizza (Create)
Once a user has logged in or registered they can add new pizzas and toppings to the database.
User can choose a name, sauce type, cheese type, choose a code, then pick up to 4 toppings per topping category.

#### Pizza Recipe Display (Read)
Pizza recipes display as cards to the user with links to edit them.

#### Edit Existing Pizza (Update)
If a user chooses to edit a pizza they will see the forms and check boxes with 
the existing data. They can then change this and either update the database or they can delete pizzas from the database

#### Delete Pizza (Delete)
Users can delete pizzas by first selecting the edit button, then selecting delete button, this was done to reduce the liklihood of accidentally deleted pizzas.

#### Pagination
Each page shows 6 recipies to the user.

#### Login/Register
User can register to the website, and once don so they have access to more features.

#### Add Topping
Users can add toppings to the database once they have logged in. They can choose to add either meat or veg to the database.

### Future Features

#### Admin Features
A seperate admin log in and general user log in. General users would be able to 
log in, browse pizzas, post pizzas, edit, or add toppings to be approved by the admin.
Only the admin would be able to approve changes and delete pizzas.

#### Add New Sauce/Cheese
Just with adding a new topping, users would be able to add new sauces or cheeses
to the database.

#### Remove Toppings
At the moment users can add and delete pizzas, but can only add toppings. 
In future users would be able to do both.

#### Archive Pizzas
The ability to not only delete pizzas, but archive pizzas. If the database was 
used for training purposes, then seasonal pizzas could be archived and brought back
at a later date.

#### Edit permissions
Currently any user can edit any pizza, in future only the user that created the recipe could edit the recipe.

#### Change User Password
At the moment users cannot change their password. But will in future.

#### Cookie Declaration
Currently there is no cookie declaration when users open the app.

#### Delete Account
Users can create a count, but cannot yet delete their account.

#### Last Updated By
Pizza cards would display "Created by: " and "Last updated by: ".

## Technologies Used
The project makes use of:
 - [HTML](https://www.w3schools.com/html/)
 -- To build the structure of the content.
 - [CSS](https://www.w3schools.com/css/default.asp) 
 -- To style the content.
 - [Chrome](https://www.google.co.uk/chrome/?brand=CHBD&gclid=CjwKCAjwg-DpBRBbEiwAEV1_-HRKc5kuXoGrUIbi1QWzng3ZEvw3Obv1qmhUoXJa2iqrfZ4IxfgntRoC_hYQAvD_BwE&gclsrc=aw.ds)
 -- A cross-platform web browser developed by Google. Used as the main browser for dev tools, and to test responsiveness.
 - [AWS cloud9](https://aws.amazon.com/cloud9/)
 -- An online IDE.
 - [GitHub](https://github.com/)
 -- Provides hosting for software development version control using Git.
 - [GitHub Pages](https://pages.github.com/)
 -- A static web hosting service offered by GitHub
 - [Responsive Design](http://ami.responsivedesign.is/)
 -- Used to screenshot web application on different devices.
 - [Google Fonts](https://fonts.google.com/)
 -- Used for 'Nunito' font.
 - [Heroku](https://www.heroku.com)
 -- Used to deploy app.
 - [jQuery](https://jquery.com/)
 -- A fast, small, and feature-rich JavaScript library. Used in this app for Materialize initialisation and checkbox limiter.
 - [Materialize](https://materializecss.com/about.html)
 -- A design language that combines the classic principles of successful design along with innovation and technology. 

## Testing

### Responsiveness
[Chrome](https://www.google.co.uk/chrome/?brand=CHBD&gclid=CjwKCAjwg-DpBRBbEiwAEV1_-HRKc5kuXoGrUIbi1QWzng3ZEvw3Obv1qmhUoXJa2iqrfZ4IxfgntRoC_hYQAvD_BwE&gclsrc=aw.ds)
Was used to test:
- Galaxy S5
- Pixel 2
- Pixel 2XL
- iPhone 5/SE
- iPhone 6/7/8
- iPhone 6/7/8 Plus
- iPhone X
- iPad
- iPad Pro
- Desktop

[Responsive Design](http://ami.responsivedesign.is/) was used to check viewports:

- Desktop
1600x992px scaled down to scale(0.3181)
- Laptop
1280x802px scaled down to scale(0.277)
- Tablet
768x1024px scaled down to scale(0.219)
- Mobile
320x480px scaled down to scale(0.219)

Page is fully responsive.

### Code Testing
[HTML Validator](https://www.freeformatter.com/html-validator.html) -- No issues found. Validator doesn't recognise Jinja.

[CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) -- No issues found.

### User Testing
Tested a small group of people (3-4), found an issue where labels were causing 
users to not be able to click on text inputs. Code was changed to replace labels with placeholders.

### Known Bugs
When a user creates a recipe the card will say it was added by that user. If a 
different user edits the recipe, it will say it was added by them.

## Deployment
The code was developed using the AWS Cloud9 IDE.

Deployed app can be viewed [here.](https://pizza-database.herokuapp.com/add_pizza)

GitHub Repo [here](https://github.com/kennedydmb/pizza-database-project)

### For local deployment
- Clone the project:
` git clone https://github.com/kennedydmb/pizza-database-project`
- Arrange contents so that the cloned document is in the root of the enviroment.
- Make sure flask, pymongo, flask_pymongo and dnspython are all installed. Something along the lines of:
```
sudo pip3 install flask

sudo pip3 install pymongo

sudo pip3 install flask_pymongo

sudo pip3 install dnspython

```
- Create a new app on Heroku and link to your local repo.
- Create a requirements.txt and Procfile.
```
sudo pip3 freeze --local > requirements.txt

echo web: python app.py > Procfile
```
- Set up evironment variables for MONGO_URI and SECRET_KEY, keep them hidden so sensitive data does not get pushed to Heroku.
- On Heroku set up config variables for PORT, ID, MONGO_URI, and SECRET_KEY.
- Push commits to Heroku:
`git push heroku master`


### Content
- Data created using current pizza shop knowledge. Some pizzas already exist in the world
some are made up by users.
- Background image of pizza cards from unsplash found [here.](https://unsplash.com/photos/JnAJSWiio64)
- Image was edited using [Paint.NET.](https://www.getpaint.net/)
- Image was hosted on [Imgur.](https://imgur.com/)

## Acknowledgements
- Code Institute for the lessons and basis for the app.
- Code Institues student Slack, extremely helpful for picking up ideas and debugging issues.
- Stack Overflow and W3Schools for finding answers to issues I was having, or to brush up on the basics.
- Some code was taken from a user on Slack and modified for the project. Miroslav Svec's (username Miro) 
sessions from the student slack channel. the code for the registration and login logic.