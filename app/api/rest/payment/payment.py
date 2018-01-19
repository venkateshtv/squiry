from flask import request
from app.api.rest.base import BaseResource, SecureResource, rest_resource
from app.api.db import get_data,insertupdate,read
import datetime
import hashlib
from random import randint

class PayU(self):
    self.key=""
	self.SALT = ""
	self.PAYU_BASE_URL = "https://sandboxsecure.payu.in/_payment"
	self.action = ''
	self.posted={}
    def create_payment_request(self,params):
        hash_object = hashlib.sha256(b'randint(0,20)')
	    txnid=hash_object.hexdigest()[0:20]
        
        return ""

gateway = "payu"
class PaymentFactory(self):

    def get_payment_gateway(gateway):
        if gateway == "payu":
            return PayU()

@rest_resource
class PaymentRequest(BaseResource):
    """ /api/paymentrequest """
    endpoints = ['/paymentrequest']

    def post(self):        
        params = request.json
        payment_gateway = PaymentFactory().get_payment_gateway(gateway)
        request = payment_gateway.create_payment_request(params)
        return request

