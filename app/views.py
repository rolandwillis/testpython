import os
from app import app
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import jsonify, send_from_directory, request
import json
import logging


logging.basicConfig(filename='app.log',level=logging.DEBUG)

class Settings:
    def __init__(self,j):
        self.user = j['user']
        self.password = j['password']
        self.server = j['server']
        self.db = j['db']
        self.port = j['port']


<<<<<<< HEAD
=======
    
sqlhub.processConnection = connectionForURI('mssql://user:pwd@server:port/PythonTest')
>>>>>>> 47d240563c78eb51860ce186524026125836d690

#settings = Settings("PythonUser","Experis123!","PythonTest","MPGSDWPSH0001",1402)
with open('config.json') as json_data_file:
    data = json.load(json_data_file)

settings = Settings(data)

engine = create_engine('mssql+pymssql://%s:%s@%s:%d/%s' % (settings.user,settings.password,settings.server,settings.port,settings.db))
Session = sessionmaker(bind=engine)
#sqlhub.processConnection = connectionForURI('mssql://%s:%s@%s:%d/%s' % (settings.user,settings.password,settings.server,settings.port,settings.db))
Base = declarative_base()
class Person(Base):
    __tablename__ = "Person"
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)


    def serialize(self):  
        return { 
            'id':self.id,          
            'firstname': self.firstname, 
            'lastname': self.lastname
        }


    
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'logo_RVB.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/Person/Get/<int:userid>', methods=['GET'])
def personget(userid):
    session = Session()
    person=session.query(Person).filter_by(id=userid).first()
        
    return jsonify(person=person.serialize())


@app.route('/Person/Update/<int:userid>', methods=['POST'])
def personupdate(userid):
 

    
    logging.info('is json = %s' % request.is_json)
    
    if (request.is_json):
        jsn= request.get_json()
        logging.info(jsn)
        session = Session()
        person=session.query(Person).filter_by(id=userid).first()
        person.lastname=jsn['lastname']
        person.firstname=jsn['firstname']
        session.commit()
        return jsonify(person=person.serialize())
    else:
        return jsonify(person=None)

@app.route('/Person/Create', methods=['POST'])
def personcreate():
 

    
    logging.info('is json = %s' % request.is_json)
    
    if (request.is_json):
        jsn= request.get_json()
        logging.info(jsn)
        session = Session()
        person=Person(firstname=jsn['firstname'],lastname=jsn['lastname'])
        session.add(person)
        session.commit()
        return jsonify(person=person.serialize())
    else:
        return jsonify(person=None)