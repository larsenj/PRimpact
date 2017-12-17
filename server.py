#!/bin/python3

#from threading import thread
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

#setup the database and Flask
db_connect = create_engine('sqlite:///test.db')
app = Flask(__name__)
api = Api(app)

#returns a json object containing 
class GetAllPoints(Resource):
    def get(self):
        conn = db_connect.connect() #connect to the database
        query = conn.execute("select * from Entries;") #select everyone in the database
        result = {'data':[dict(zip(tuple(query.keys()) ,i )) for i in query.cursor]}
        return jsonify(result)


class Entries(Resource):

    ''' 
    #Need to figure out conversion of lat-lon distances to km 
    #get all entries within specific radius
    def get(self, lat, lon):
        conn = db_connect.connect()
        query = conn.execute()
        result = {'data':[dict(zip(tuple(query.keys()) ,i )) for i in query.cursor]}
        return jsonify(result)
    '''
    #will need to figure out rough lat/lon conversions into 
    def post(self):
        conn = db_connect.connect()
        print(request.json)
        mac = request.json['mac']
        food = request.json['food']
        water = request.json['water']
        power = request.json['power']
        lat = request.json['lat']
        lon = request.json['lon']
        query = conn.execute("INSERT INTO Entries \
        VALUES('{0}', '{1}','{2}','{3}','{4}','{5}');".format(mac, food,
            water, power, lat, lon))
        return{'status':'success'}


api.add_resource(GetAllPoints, '/all')
api.add_resource(Entries, '/Entries')


if __name__ == "__main__":

    #check for correct usage
    '''
    if len(sys.argv) < ???????????????:
        print 'Usage: python server.py [hostname] [server port] 
        sys.exit()
    '''

    #TODO: use arg for port
    app.run(port='5002')

'''
    try:
        Thread(target=Command).start()
        #Thread(target=AddData).start()
        #Thread(target=GetData).start()
    except:
        print "Error initializing threads"
'''
