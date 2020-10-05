# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api


import socket,os

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class greetings(Resource):
    def get(self):
        return {'hello world from':'Hostname_'+ str(os.getpid())+socket.gethostname() }

class square(Resource):
    def get(self, num): 
        return {'square': num**2} 

#endpoints
api.add_resource(HelloWorld, '/') 
api.add_resource(greetings, '/greetings')
api.add_resource(square, '/square/<int:num>')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

