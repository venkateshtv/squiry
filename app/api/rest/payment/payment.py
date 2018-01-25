import datetime
import hashlib
import uuid
from random import randint
import barcode
from barcode.writer import ImageWriter
from flask import request
from app.api.rest.base import BaseResource, SecureResource, rest_resource
from app.api.db import get_data,insertupdate,read
from app.api.utils.mail import send_mail
import os

class PayU():
    #XZYmyU9I
    #zo7yEZu9UZ
    #key="gtKFFx"
    #SALT = "eCwWELxi"
    #PAYU_BASE_URL = "https://sandboxsecure.payu.in/_payment"
	
    def create_transaction(self,params):        
        query = "INSERT INTO transactions"
        query += """  (eventid,paymentstatus,amount,useremail,userphonenumber,createddate)"""
        query += """ VALUES ({},'{}',{},'{}',{},'{}') RETURNING txnid"""
        query = query.format(params.get('productinfo'),'initiated',params.get('amount'),params.get('email'),params.get('phone'),str(datetime.datetime.now()))
        return insertupdate(query)
        
    def create_payment_request(self,params):
        # key="XZYmyU9I"
        # SALT = "zo7yEZu9UZ"
        key="gtKFFx"
        SALT = "eCwWELxi"
        PAYU_BASE_URL = "https://sandboxsecure.payu.in/_payment"
        hash_object = hashlib.sha256(b'randint(0,20)')
        #txnid= uuid.uuid4().int#params.get('phone')+datetime.datetime.now().strftime("%Y%m%d%H%M")#hash_object.hexdigest()[0:20]
        params['key']= key        
        params['txnid'] = self.create_transaction(params).get('txnid') + '345676'
        print("TXNID", params['txnid'])
        hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
        hash_string=''
        hashVarsSeq= hashSequence.split('|')        
        for i in hashVarsSeq:
            try:
                hash_string+= str(params.get(i,''))                
            except Exception as e:                
                hash_string+=''
            hash_string+='|'
        hash_string+= SALT
        print("HASH",hash_string)
        hashh= hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()
        return {'txnid':params['txnid'],'merchant_key':key,'hash':hashh}
    
    def validate_payment_request(self,request_params):
        status=request_params["status"]
        firstname=request_params["firstname"]
        amount=request_params["amount"]
        txnid=request_params["txnid"]
        posted_hash=request_params["hash"]
        key=request_params["key"]
        productinfo=request_params["productinfo"]
        email=request_params["email"]
        udf1 = request_params["udf1"]
        udf2 = request_params["udf2"]
        udf3 = request_params["udf3"]
        udf4 = request_params["udf4"]
        udf5 = request_params["udf5"]
        salt="eCwWELxi"
        try:
            additionalCharges=request_params["additionalCharges"]
            retHashSeq=additionalCharges+'|'+salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
        except Exception:
            retHashSeq = salt+'|'+status+'||||||'+ udf5 +'|'+ udf4 +'|'+ udf3 +'|'+ udf2 +'|'+ udf1 +'|'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
        hashh=hashlib.sha512(retHashSeq.encode('utf-8')).hexdigest().lower()
        #updatedb
        bcc = ["venkateshtv@outlook.com","prakashkumar_d@outlook.com"]
        if(hashh !=posted_hash):
            print ("Invalid Transaction. Please try again")
            msg = """<html> <head></head> <body> """
            msg += """Hi <b>{}</b> <br/>""".format(firstname)
            msg += """ We have received an invalid trasaction with id {} <br/> Please mail to info@squiry.in for any questions. <br/> Thank you, <br/> Squiry team""".format(txnid)
            msg += """ </body></html> """
            send_mail(email,bcc,"Payment failure from Squiry", msg,False)
            return {"validtransaction":'false',"message":'Invalid Transaction. Please try again'}            
        else:
            barcode = self.create_barcode(txnid)
            self.update_barcode(txnid,barcode)
            message = """<html> <head></head> <body> """
            message += """ Hi <b>{}</b><br/>""".format(firstname)
            message += """ Thank you for registering to our event <b>{}</b> <br/>""".format(udf1)
            message += """We have received a payment of Rs. <b>{}</b>""".format(amount)
            message += """Your Transaction ID for this transaction is {} <br/>""".format(txnid)            
            message += """ Here are the event details: <br/> """
            message += """ <img src='https://squiryapp.herokuapp.com/dist/barcodes/{}'></img> """.format(barcode+'.png')
            message += """ <i>Date & Time: {}</i><br/>""".format(udf3)
            message += """ <i>Address {}</i><br/><br/>""".format(udf2)
            message += """ Have a nice time <br/> Please send your questions to info@squiry.in <br/>"""
            message += """ Thank you, <br/> Squiry Team"""
            message += """ </body></html> """
            message += send_mail(email,bcc,"Payment success from Squiry", message,False)
            return {"validtransaction":'true',"message":message}
       
    def failed_transaction(self,request_params):
        #update db
        #Send Mail
        print ("Failed Transactions")

    def random_with_N_digits(self,n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        print("N",n)
        print("RANGE",range_start)
        print("RANGE",range_end)
        return randint(range_start, range_end)

    def create_barcode(self,txnid):
        num_to_generate = 0
        barcode_string = str(txnid)        
        if len(barcode_string) < 13:
            num_to_generate = 13-len(barcode_string)
            ran_num = self.random_with_N_digits(num_to_generate)
            barcode_string += str(ran_num)
        
        print("Barcode string",barcode_string)

        ean = barcode.get('ean13',barcode_string, writer=ImageWriter())    
        path = os.path.join(os.path.abspath(os.curdir),'app','client','app','barcodes',str(barcode_string))
        file = ean.save(path)
        print("FULL NAME OF FILE",file)
        return barcode_string

    def update_barcode(self,id,barcode):
        query = """ UPDATE transactions set barcode= {} where id = {}""".format(barcode,id)
        return insertupdate(query)

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

