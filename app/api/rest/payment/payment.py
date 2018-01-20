import datetime
import hashlib
from random import randint
from flask import request
from app.api.rest.base import BaseResource, SecureResource, rest_resource
from app.api.db import get_data,insertupdate,read

class PayU():
    #XZYmyU9I
    #zo7yEZu9UZ
    #key="gtKFFx"
    #SALT = "eCwWELxi"
    #PAYU_BASE_URL = "https://sandboxsecure.payu.in/_payment"
	
    def create_payment_request(self,params):
        key="gtKFFx"
        SALT = "eCwWELxi"
        PAYU_BASE_URL = "https://sandboxsecure.payu.in/_payment"
        hash_object = hashlib.sha256(b'randint(0,20)')
        txnid=params.get('phone')+datetime.datetime.now().strftime("%Y%m%d%H%M")#hash_object.hexdigest()[0:20]
        params['key']= key
        params['txnid'] = txnid
        hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
        hash_string=''
        hashVarsSeq= hashSequence.split('|')
        print("Seq Array",hashVarsSeq)
        for i in hashVarsSeq:
            try:
                hash_string+= str(params.get(i,''))                
            except Exception as e:                
                hash_string+=''
            hash_string+='|'
        hash_string+= SALT
        print("HASH",hash_string)
        hashh= hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()
        return {'txnid':txnid,'merchant_key':key,'hash':hashh}
    
    def validate_payment_request(self,request_params):
        status=request_params["status"]
        firstname=request_params["firstname"]
        amount=request_params["amount"]
        txnid=request_params["txnid"]
        posted_hash=request_params["hash"]
        key=request_params["key"]
        productinfo=request_params["productinfo"]
        email=request_params["email"]
        salt="eCwWELxi"
        try:
            additionalCharges=request_params["additionalCharges"]
            retHashSeq=additionalCharges+'|'+salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
        except Exception:
            retHashSeq = salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
        hashh=hashlib.sha512(retHashSeq.encode('utf-8')).hexdigest().lower()
        if(hashh !=posted_hash):
            print ("Invalid Transaction. Please try again")
            return {"validtransaction":'false',"message":'Invalid Transaction. Please try again'}            
        else:
            message = "Thank You. Your order status is " + status +"\n"
            message += "Your Transaction ID for this transaction is " +txnid +"\n"
            message += "We have received a payment of Rs. "+  amount +". Please check your mail for more details"
            return {"validtransaction":'true',"message":message}


gateway = "payu"
class PaymentFactory():

    def get_payment_gateway(self,gateway):
        if gateway == "payu":
            return PayU()

@rest_resource
class PaymentRequest(BaseResource):
    """ /api/paymentrequest """
    endpoints = ['/paymentrequest']

    def post(self):        
        params = request.json
        print("PARAM",params)
        payment_gateway = PaymentFactory().get_payment_gateway(gateway)
        payment_request = payment_gateway.create_payment_request(params)
        return payment_request

