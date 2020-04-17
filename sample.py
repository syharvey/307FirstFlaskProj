from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import string
import random

app = Flask(__name__)
CORS(app)

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

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      if search_username :
         subdict = {'users_list' : []}
         search_job = request.args.get('job')
         if search_job : 
             for user in users['users_list']:
                if user['name'] == search_username and user['job'] == search_job:
                    subdict['users_list'].append(user)
         else:
             for user in users['users_list']:
                if user['name'] == search_username:
                    subdict['users_list'].append(user)
         return subdict
         
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd['id'] = getRandomId(); 
      users['users_list'].append(userToAdd)
      resp = jsonify(userToAdd)
      #resp = jsonify(success=True)
      resp.status_code = 201 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp
   elif request.method == 'DELETE':
      search_username = request.get_json()
      #search_username = request.args.get('id')
      if search_username :
        for user in users['users_list']:
          if user == search_username:
             users['users_list'].remove(user)
             resp = jsonify(success=True)
             resp.status_code = 200 #optionally, you can always set a response code. 
             return resp

def getRandomId() :
        return ''.join(random.choices(string.ascii_lowercase+string.digits,k=6))

@app.route('/users/<id>', methods=['GET','DELETE'])
def get_user(id):
   if request.method == 'GET':
      if id :
        for user in users['users_list']:
          if user['id'] == id:
            return user
        return ({})
      return users
   if request.method == 'DELETE':
      #search_username = (request.get_json())['id']
      #search_username = request.args.get('id')
      print("user to delete");
      print(id);
      #search_username = request.args.get('id')
      #if search_username :
      for user in users['users_list']:
        if user['id'] == id:
           print(user)
           print()
           users['users_list'].remove(user)
      resp = jsonify(success=True)
      resp.status_code = 200 #optionally, you can always set a response code. 
      return resp

