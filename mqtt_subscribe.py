import paho.mqtt.client as mqtt
import time

import smtplib
import ssl
from email.message import EmailMessage

import mimetypes
import os

def sendMail(packet):
            print("STARTED to send Mail ...")

            #-----------------start-------------
            
            email_sender = '124158009@sastra.ac.in'
            email_password = 'dmjc fyxl msya fqez'
            email_receiver = 'arunbalaji211@gmail.com'
            subject ="Received Temperature " 
            body='''ALERT ...
                    HIGH
                    TEMP \n'''+packet
            
            print("The temp message as an body content...")
            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['subject'] = subject
            em.set_content(body)

            print("Attached the message as body to the EmailMessenge() obj ")
           
            #---------started modification-----------
            
            attachment_path = "ht.jpg"
            
            attachment_filename = os.path.basename(attachment_path)
            
            mime_type, _ = mimetypes.guess_type(attachment_path)
            
            mime_type, mime_subtype = mime_type.split('/', 1)
            
            with open(attachment_path, 'rb') as ap:
                   em.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype,filename=os.path.basename(attachment_path))            
           
            print("----ATTACHED SUCCESSFULLY-----")
            
            #----------modification done------
            
            
            #   using smtp_ssl
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())

            print("Mail Sent to the ",em['To'])
            #------------------end of function ---------------

def on_message(client, userdata, message):

    packet=str( message.payload.decode("utf-8") )   
    print("received message: " ,str(packet)) 
    if( float(packet) >=30.0 ):
        #print("HIGH TEMP :")
        #------sendMail()------
        sendMail(packet)
        
            
mqttBroker ="mqtt.eclipseprojects.io"
client = mqtt.Client("TEMPERATURE_HOME") 
client.connect(mqttBroker)

client.loop_start()

client.subscribe("TEMPERATURE") 
client.on_message=on_message
#sendMail()

time.sleep(30)
client.loop_stop()