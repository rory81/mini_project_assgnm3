import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

# is to connect to the right database (here:taskmanager)
app.config["MONGO_DBNAME"] = 'taskmanager'
# optional voor de pymongo version we are using
app.config["MONGO_URI"] = 'mongodb+srv://rory81:<>@myfirstcluster-nn45a.mongodb.net/task_manager?retryWrites=true&w=majority'


# create an instance of PyMongo and then add the app into that
mongo = PyMongo(app)

# setup connection to the database
# routing (@) is a string that, when attach it to a URL, will redirect to a particular function in our Flask application
@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
