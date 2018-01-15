from flask import request
from app.api.rest.base import BaseResource, SecureResource, rest_resource
from app.api.rest.events.event import Event
from app.api.db import get_data,insertupdate,read

@rest_resource
class SquiryPicksEvents(BaseResource):
    """ /api/squirypicksevents """
    endpoints = ['/squirypicksevents']

    def get(self):        
        return read("select e.id,e.name,e.location,e.url,e.eventstart,c.name as categoryname from squirypicks s inner join event e on s.eventid=e.id inner join eventcategory c on e.categoryid = c.id;")

@rest_resource
class TopEvents(BaseResource):
    """ /api/topevents """
    endpoints = ['/topevents/','/topevents/<string:category>']

    def get(self,category = None):        
        return read("select e.id,e.name,e.location,e.url,e.eventstart,c.name as categoryname from topevents t inner join event e on t.eventid=e.id inner join eventcategory c on e.categoryid = c.id;")

@rest_resource
class EventCategories(BaseResource):
    """ /api/eventcategories """
    endpoints = ['/eventcategories']

    def get(self,category = None):                
        categories = read("select * from eventcategory;")          
        return categories

@rest_resource
class EventDetails(BaseResource):
    """ /api/event """
    endpoints = ['/event/<string:eventname>/<int:eventid>']

    def get(self,eventname,eventid):                
        event = read("select *,c.name as categoryname from event e inner join eventcategory c on e.categoryid = c.id where e.name='{}' and e.id='{}';".format(eventname,eventid), False)          
        if(event):
            prices = read("select * from price where eventid = {}".format(eventid))
            if prices != None:
                event['prices'] = prices
        return event