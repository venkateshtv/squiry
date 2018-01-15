from flask import request
from app.api.rest.base import BaseResource, SecureResource, rest_resource
from app.api.rest.events.event import Event
from app.api.db import get_data,insertupdate,read

apiKey = "p69369"
@rest_resource
class AddEvent(BaseResource):
    """ /api/addevent """
    endpoints = ['/addevent']

    def post(self):
        event = request.json
        if(event.apiKey == None):
            raise Exception("API Key required")
        if(event.apiKey != apiKey):
            raise Exception("API Key doesn't match")
        query = "INSERT INTO event (name,description,address,location,latlong,url,eventstart,eventend,categoryid) VALUES ({},{},{},{},{},{},{},{},{})"
        query = query.format(event.get('name'),event.get('description',''),event.get('address',''),event.get('location',''),event.get('latlong',''),event.get('url',''),event.get('eventstart',''),event.get('eventend',''),event.get('categoryid',''))
        return insertupdate(query)

@rest_resource
class UpdateEvent(BaseResource):
    """ /api/updateevent """
    endpoints = ['/updateevent']

    def post(self):
        event = request.json
        query = "UPDATE event SET "
        setQuery =""
        if(event.apiKey == None):
            raise Exception("API Key required")
        if(event.apiKey != apiKey):
            raise Exception("API Key doesn't match")
        for key in event:
            value = event.get(key)
            if value != None:
                setQuery += ","+key+"="+value
        if setQuery is "":
            raise "Nothing to update"
        setQuery = setQuery.strip(',')
        query = query + setQuery + "where id =" +event.get('id')
        return insertupdate(query)

