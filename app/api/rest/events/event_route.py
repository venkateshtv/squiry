from flask import request
from app.api.rest.base import BaseResource, SecureResource, rest_resource
from app.api.rest.events.event import Event
from app.api.db import get_data

@rest_resource
class SquiryPicksEvents(BaseResource):
    """ /api/squirypicksevents """
    endpoints = ['/squirypicksevents']

    def get(self):
        return get_data(0,4)

    def post(self):
        json_payload = request.json
        return [{'name': 'Resource Post'}]

@rest_resource
class TopEvents(BaseResource):
    """ /api/topevents """
    endpoints = ['/topevents/','/topevents/<string:category>']

    def get(self,category = None):        
        return get_data(5,10)

    def post(self):
        json_payload = request.json
        return [{'name': 'Resource Post'}]


@rest_resource
class EventCategories(BaseResource):
    """ /api/eventcategories """
    endpoints = ['/eventcategories']

    def get(self,category = None):        
        return [{"name":'Music & Night life'},{"name":'Live shows'},{"name":"Concerts"},{"name":'Art & Theatre'},{"name":'Adventure'}]

    def post(self):
        json_payload = request.json
        return [{'name': 'Resource Post'}]
