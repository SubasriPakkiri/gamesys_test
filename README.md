# gamesys_test
This is a demo application that shows how to build a RESTful web service that can queried for following based on the REVENUE_ANALYSIS dataset:

•	the total win amount for a given member,
•	the total wager amount for a given member, and
•	the number of wagers placed by a given member.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This application uses the following:

 - Python 3.5
 
### Setting up the project

First, clone this repository to your local machine:

```sh
 $ git clone https://github.com/senthilrajendran1/gamesys_test.git
```

### Running the App

To get the app running:

 - From a command line, make sure you are in the project's root folder - `gamesys_test`
 
 - Create a virtual environment:
 ```
 python -m venv env
 ```
 - Activate the virtual environment:
 ```
   source env/Scripts/activate
 ```
 On windows? Activate it with the below:
 ```
   env\Scripts\activate
 ```

 - Install the dependencies:
 ```
 pip install -r requirements.txt
 ```

 - Finally run the app:
 ```
  cd gamesys
  flask run
 ```

 Congrats! The app should now be running on http://localhost:5000.


- Open your browser and fire up the app - http://localhost:5000/

- Total Win Amount - http://localhost:5000/members/total_wins/<member_id>/<activity_month>/<game_id>
- Total Wager Amount - http://localhost:5000/members/total_wagers/<member_id>/<activity_month>/<game_id>
- Number of Wagers Placed - http://localhost:5000/members/wagers_placed/<member_id>/<activity_month>/<game_id>

## Built With

* [Flask](http://flask.pocoo.org/) - A microframework for Python
* [SQLAlchemy](https://www.sqlalchemy.org/) - A Python SQL toolkit and Object Relational Mapper
