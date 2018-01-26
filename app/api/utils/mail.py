
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sendgrid
import os
from sendgrid.helpers.mail import *

def send_mail(recipient,bcc,subject,body,params):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("donotreply@squiry.in")
    to_email = Email(recipient)
    content= Content("text/html",body)
    mail = Mail(from_email,subject,to_email,content)
    if(params != None):
        mail.personalizations[0].add_substitution(Substitution("-transactionid-", params['transactionid']))
        mail.personalizations[0].add_substitution(Substitution("-eventname-", params['eventname']))
        mail.personalizations[0].add_substitution(Substitution("-eventtime-", params['eventtime']))
        mail.personalizations[0].add_substitution(Substitution("-eventaddress-", params['eventaddress']))
        mail.personalizations[0].add_substitution(Substitution("-amount-", params['amount']))
        mail.personalizations[0].add_substitution(Substitution("-firstname-", params['firstame']))
        mail.template_id= "ce05523a-5a62-4c17-8197-5cb702387214"
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
    return True

def send_mail_smtp(recipient,bcc,subject,body,isPlain):

    try:        
        print('entering mail')
        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = 'donotreply@squiry.in'
        msg['To'] = recipient
        toAddr = recipient #[recipient,bcc]
                  
        #if bcc:
        #    msg['BCC'] = ",".join(i for i in bcc)
            #toAddr.append(bcc)
        
        # Record the MIME types of both parts - text/plain and text/html.
        
        part1 = MIMEText(body, 'plain')
        msg.attach(part1)
    
        part2 = MIMEText(body, 'html')
        msg.attach(part2)

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        print('attempting to connect mail server')
        # Send the message via local SMTP server.
        server = smtplib.SMTP('mail.squiry.in',25)
        server.ehlo()
        server.starttls()
        server.login('donotreply@squiry.in','Squiry123')
        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.
        print('sending mail ....')
        server.sendmail(recipient, toAddr, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print("Exception in sending mail",e)
        return False