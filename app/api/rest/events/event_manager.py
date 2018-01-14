from flask import request
from app.api.rest.base import BaseResource, SecureResource, rest_resource
from app.api.rest.events.event import Event
from app.api.db import get_data,insertupdate,read

@rest_resource
class AddEvent(BaseResource):
    """ /api/addevent """
    endpoints = ['/addevent']

    def post(self):
        event = request.json
        query = "INSERT INTO event (name,description,address,location,latlong,url,eventtime,categoryid) VALUES ("+event.get('name')+","+event.get('description','')+","+event.get('address','')+","+event.get('latlong','')+","+event.get('url','')+","+event.get('eventtime')+","+event.get('categoryid')+")"
        return insertupdate(query)

@rest_resource
class UpdateEvent(BaseResource):
    """ /api/updateevent """
    endpoints = ['/updateevent']

    def post(self):
        event = request.json
        query = "UPDATE event SET "
        setQuery =""
        for key in event:
            value = event.get(key)
            if value != None:
                setQuery += ","+key+"="+value
        if setQuery is "":
            raise "Nothing to update"
        setQuery = setQuery.strip(',')
        query = query + setQuery + "where id =" +event.get('id')
        return insertupdate(query)

