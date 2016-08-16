from app import app
from sqlobject import *
from flask import jsonify

    
sqlhub.processConnection = connectionForURI('mssql://PythonUser:Experis123!@MPGSDWPSH0001:1402/PythonTest')

class Person(SQLObject):
    firstname = StringCol()
    lastname = StringCol()

    def serialize(self):  
        return {           
            'firstname': self.firstname, 
            'lastname': self.lastname
        }


    


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/GetIn')
def getin():
    return "Get In!"

@app.route('/FindMe/<user>')
def findme(user):
    return user

@app.route('/Post/<int:userid>')
def post(userid):
    person=Person.get(userid)
    return jsonify(person=person.serialize())


