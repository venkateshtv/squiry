from flask import request
from app.api.rest.base import BaseResource, SecureResource, rest_resource
from app.api.rest.events.event import Event
from app.api.db import get_data,insertupdate,read

@rest_resource
class SquiryPicksEvents(BaseResource):
    """ /api/banners """
    endpoints = ['/banners']

    def get(self):        
        return read("""select e.id,e.name,e.location,e.url,e.eventstart,c.name as categoryname from banners s inner join event e on s.eventid=e.id inner join eventcategory c on e.categoryid = c.id;""")

@rest_resource
class TopEvents(BaseResource):
    """ /api/topevents """
    endpoints = ['/topevents/','/topevents/<string:category>']

    def get(self,category = None):        
        return read("""select e.id,e.name,e.location,e.url,e.eventstart,c.name as categoryname from topevents t inner join event e on t.eventid=e.id inner join eventcategory c on e.categoryid = c.id;""")

@rest_resource
class EventCategories(BaseResource):
    """ /api/eventcategories """
    endpoints = ['/eventcategories']

    def get(self,category = None):                
        categories = read("select * from eventcategory order by name asc;")          
        return categories

def get_prices(eventid):
    return read("""select * from price where eventid = {}""".format(eventid))

def get_discounts(eventid):
    return read("""select * from discounts where eventid = {}""".format(eventid))

@rest_resource
class EventDetails(BaseResource):
    """ /api/event """
    endpoints = ['/event/<string:eventname>/<int:eventid>']

    def get(self,eventname,eventid):                
        event = read("""select e.*,c.name as categoryname from event e inner join eventcategory c on e.categoryid = c.id where e.name='{}' and e.id={};""".format(eventname,eventid), False)          
        if(event):
            print("Event  ",event)
            prices = get_prices(event['id']) 
            print("Prices")
            print(prices) 
            if prices != None:
                event['prices'] = prices
            discounts = get_discounts(event['id'])
            print("Discount")
            print(discounts) 
            if discounts != None:
                event['discounts'] = discounts
        return event

@rest_resource
class Discount(BaseResource):
    """ /api/verifydiscountcoupon """
    endpoints = ['/verifydiscountcoupon/<int:eventid>/<string:couponcode>']

    def get(self,eventid,couponcode):
        discount = read((""" select discountname,discounttype from discounts where eventid = {} and couponcode = '{}';""").format(eventid,couponcode), False)
        if discount is not None:
            return {"verified":"true", "discountname": discount['discountname'], "discounttype": discount['discounttype']}
        else:
            return {"verified":"false"} 