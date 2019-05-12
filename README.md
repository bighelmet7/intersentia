Sandwich ordering
=================

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

TODO
----

* Order app and /api/v1/orders/ endpoint for consulting all the deliveries.
* /toppings for the frontend.
* Login users
* Current month information of a given user.

Concept
--------

Sandwich ordering is a proposal exercice of Intersentia for creating an ORM dashboard with Flask.

Technologies
---------

Flask is our main backend service with some third parties apps as Flask-Restful, Flask-Migrate and Flask-Api for a more
easy-to-use experience. Connected to a locally SQLite database.

React for the frontend dashboard and some thrid parties apps specified in the package.json


API
---

Available endpoints:
- /api/v1/bars/
- /api/v1/bars/<bar:id>/
- /api/v1/bars/<bar:id>/sandwiches/
- /api/v1/bars/<bar:id>/sandwiches/<sandwich:id>/
