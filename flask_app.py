from flask import Flask,request,jsonify
import json
from tasks import *
from accounts import *

 
app = Flask(__name__)

@app.route('/register',methods=["POST"])
def register():
    req_data = json.loads(request.data.decode('utf-8'))
    name = req_data['name']
    password =req_data['password']
    accounts[name] = password
    return jsonify("Thanks for signing up " + name),201

@app.route('/login', methods=['POST'])
def login_user():
    req_data = json.loads(request.data.decode('utf-8'))
    username=req_data['username']
    password =req_data['password']
    return jsonify("you have logged in" + username)



@app.route('/tasks', methods=["POST"])
def add_task():
    task_data=json.loads(request.data.decode('utf-8'))
    title=task_data['title']
    new_task={'title':title}
    todo_list.append(new_task)
    return jsonify({
        "message":"You have created task"}) , 201

@app.route('/tasks/<string:title>', methods=['DELETE'])
def delete_a_task(title):

    for task in range(len(todo_list)):
        if task['title'] == title:
            del todo_list[task]
            return"You have deleted {}".format(task)

@app.route('/tasks', methods=['DELETE'])
def delete_all_tasks():
    todo_list.clear()
    return "You have deleted all tasks"


@app.route('/tasks/<string:title>', methods=['PUT'])
def mark_as_finished(title):
    task_data=json.loads(request.data.decode('utf-8'))
    title=task_data['title']
    
    for key in task_status.items():
        if key == title:
            task_status[key] = "Finished"
            return task_status
                
    

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
