from flask import request
from app.api.rest.base import BaseResource, SecureResource, rest_resource
from app.api.rest.events.event import Event
from app.api.db import get_data,insertupdate,read
import os

def addPrices(prices,eventid):
    for price in prices:
        pricequery = "INSERT INTO price(name,price,quantity,eventid) values('{}',{},{},{}) RETURNING id;"
        insertupdate(pricequery.format(price.get('name'),price.get('price'),price.get('quantity'),eventid))


apiKey = "p69369"
@rest_resource
class AddEvent(BaseResource):
    """ /api/addevent """
    endpoints = ['/addevent']
    
    def post(self):
        event = request.json
        if(event.get('apiKey') == None):
            raise Exception("API Key required")
        if(event.get('apiKey') != apiKey):
            raise Exception("API Key doesn't match")        
        query = 'INSERT INTO event (name,description,address,location,latlong,url,eventstart,eventend,categoryid) VALUES ("{}","{}","{}","{}","{}","{}","{}","{}",{}) RETURNING id;'
        query = query.format(event.get('name'),event.get('description',""),event.get('address',""),event.get('location',""),event.get('latlong',"''"),event.get('url',""),event.get('eventstart',""),event.get('eventend',""),event.get('categoryid',0))
        eventresult = insertupdate(query)
        print("EVENTS RESULT")
        print(eventresult)
        prices = event.get('prices')
        addPrices(prices,eventresult.get('id'))
        return eventresult       

@rest_resource
class UpdateEvent(BaseResource):
    """ /api/updateevent """
    endpoints = ['/updateevent']

    def post(self):
        event = request.json
        query = "UPDATE event SET "
        setQuery =""
        if(event.get('apiKey') == None):
            raise Exception("API Key required")
        if(event.get('apiKey') != apiKey):
            raise Exception("API Key doesn't match")
        for key in event:
            value = event.get(key)
            if value != None:
                setQuery += ","+key+"="+value
        if setQuery is "":
            raise "Nothing to update"
        setQuery = setQuery.strip(',')
        query = query + setQuery + "where id =" +event.get('id') +";"
        return insertupdate(query)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@rest_resource
class UploadEventImage(BaseResource):
    """ /api/uploadeventimage """
    endpoints = ['/uploadeventimage']

    def post(self):
        imagefile = request.files['file']
        print("file")
        print(imagefile)
        if imagefile:
            path = os.path.join(os.path.abspath(os.curdir),'app','client','app','images',imagefile.filename)
            imagefile.save(path)
            return "dist/images/{}".format(imagefile.filename)
        else:
            print("Exception occurred")
            raise Exception("No image file found")
        
