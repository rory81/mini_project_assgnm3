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


@app.route('/add_task')
def add_task():
    return render_template("addtask.html",
                           categories=mongo.db.categories.find())


@app.route('/insert_task', methods=['POST'])
def insert_task():
    tasks = mongo.db.tasks
    # when you submit information to a URI/weblocation it is submitted in the form of a request object
    tasks.insert_one(request.form.to_dict())  # the request is converted to a dictionary so it can easily be understood by Mongo
    return redirect(url_for('get_tasks'))  # redirect to get_tasks so you can see the that the new task is added

"""
@app.route('/update_task/<task_id>', methods=['POST'])
def update_task(task_id):
    tasks = mongo.db.tasks
    tasks.update(
        {'_id': ObjectId(task_id)},
        {
            'task_name': request.form.get('task_name'),
            'category_name': request.form.get('category_name'),
            'task_description': request.form.get('task_description'),
            'due_date': request.form.get('due_date'),
            'is_urgent': request.form.get('is_urgent')
        }
    )
    return redirect(url_for('get_tasks'))
"""

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
