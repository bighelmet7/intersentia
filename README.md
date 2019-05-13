Sandwich ordering
=================

![alt text](https://github.com/bighelmet7/intersentia/blob/master/sandwich_order.png "Main dashboard")



Requirements
------------

- Virtualenv
- Python 2.7
- Yarn

Installation
------------

Python packages:
```
pip installs -r requirements.txt
```
JS dependencies:
```
cd static/
yarn install
```

Local Run
---------

For running the backend service.
```
python app.py
```
And for creating a new bundle.js
```
yarn build
```

TODO
----

* Create order app and /api/v1/orders/ endpoint for consulting all the deliveries.
* /toppings for the frontend.
* Login users
* Current month information of a given user.
* API filtering by parameters.
* Swagger api with flask swagger for a more pretty documentation.
* manage.py for the Flask app.
* API testing.

Concept
--------

Sandwich ordering is a proposal exercice of Intersentia for creating an ORM dashboard with Flask.

Technologies
---------

Flask is our main backend service with some third parties apps as Flask-Restful, Flask-Migrate and Flask-Api for a more
easy-to-use experience. Connected to a locally SQLite database.

React for the frontend dashboard and some thrid parties apps specified in the package.json


Classes Structure
-----------------

The Bar class stores a name, an email (for orders), is_shop_day a boolean that tells if its the current shop of the day and
a sandwiches field that is interpreted as the "menu" of the bar. A sandwich also has it owns toppings.

It was thought this way solving the problem of same Sandwich or same Topping or a tuple of both that's duplicate a cross many bars. For example Bar A has a Cheese sandwich an Bar B also has a Cheese sandwich, but in fact Bar B its who cooks the bests Cheeses sandwiches, so the employees could know when its a good moment for ordering a cheese sandwich.

The Order class stores a number of lines orders. The lines were created by the employees, then all of those will be wrapped and create a order day instances that will be render as a HTML email.

Talking about the User class the main attributes are the is_admin and is_manager, where the first one specify an administrator and the second one a manager (only has CRUD for Bar, Sandwich and Toppings), if these two are false represents a normal employee.


Flask Structure
----------------

```
src/
├── bar
│   └── tests
├── intersentia
├── migrations
│   └── versions
├── order
├── static
│   ├── dist
│   ├── js
│   │   └── components
│   └── public
├── user
├── utils
└── v1
    ├── fields
    └── resources
```

- intersentia has the main core functionalities as extensions, config, database, exceptions and the local database.
- bar, v1 and user are some of the apps.
- static contains all the frontend logics.
- migrations its a flask migrate stuff.

API
---

Available endpoints:
- /api/v1/bars/
- /api/v1/bars/<bar:id>/
- /api/v1/bars/<bar:id>/sandwiches/
- /api/v1/bars/<bar:id>/sandwiches/<sandwich:id>/
- /api/v1/bars/<bar:id>/sandwiches/<sandwich:id>/toppings/
- /api/v1/bars/<bar:id>/sandwiches/<sandwich:id>/toppings/<topping:id>
- /api/v1/users/
- /api/v1/users/<user:id>


Testing
-------

In the bar/tests/ directory we can find a simple template of a database mock with factory_boy using the SQLAlchemy system. The main idea it is to create a mock database that handles gracefully our models and then all its remove automatically.


Problems
--------

In most of the source code are TODO, INFO and FIX comments that scopes the problem. But the main and truely problem was the time, because of my degree and my current work tasks blocks me for going further.
