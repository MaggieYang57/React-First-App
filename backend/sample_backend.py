from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import string
from model_mongodb import User

app = Flask(__name__)
CORS(app)

def randomID():
   return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)])

@app.route('/')
def hello_world():
    return 'Hello, World!'

#converted to DB version
@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      if search_username and search_job:
         subdict = {"users_list" : []}
         for user in User().find_all():
            if user["name"] == search_username and user["job"] == search_job:
               subdict["users_list"].append(user)
         return subdict
      elif search_username :
         users = User().find_by_name(search_username)
      else:
         users = User().find_all()
      return {"users_list": users}
   elif request.method == 'POST':
      userToAdd = request.get_json()
      newUser = User(userToAdd)
      newUser.save()
      resp = jsonify(newUser), 201
      return resp

#converted to DB version
@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
   if request.method == 'GET':
      user = User({"_id":id})
      if user.reload() :
         return {"users_list": user}
      else :
         return jsonify({"error": "User not found"}), 404
   elif request.method == 'DELETE': 
      user = User({"_id":id})
      if user.reload():
         user.remove()
         resp = jsonify(),204
         return resp    
      else :
         return jsonify({"error": "User not found"}), 404

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}