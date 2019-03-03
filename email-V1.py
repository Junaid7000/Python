'''
    This Script is used to Send mail to any given email adress using python's SMTPlib (Simple mail transfer protocol).
    User can add attachments like screenshot

    Author:   junaid shaikh

    Date:     27-Feb-2019, Wed, 2146hrs

'''


#import libs
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 


class SendMail():

    def __init__(self):

        #email address of PYTHON
        self.email_id = 'example@example.com'       #change this to your email id

        #password
        self.password = 'password'          #change this to your password

        #instance of message
        self.message = MIMEMultipart()              

    
    '''
    This function is used to get message from the user.

    input:  message (string) : message to send through mail.

    output: None

    '''
    def write_message(self,sub, rx_message, ):
        
        #attach subject
        self.message['Subject'] = sub

        # attach the body with the message
        self.message.attach(MIMEText(rx_message, 'plain')) 


    
    '''
    This function is used to get recievers email id.

    input: 
            rx_email(list) = email adress of reciever
 
    '''
    def to_email(self, rx_email):

        #storing recievers email
        self.message['To'] = rx_email



    '''
    This function is used to attach image with the email

    input:
            image_loc(string) = location of image
            attachment_name (strinig) = name of image or attachment

    '''

    def attach(self, image_loc, attachment_name):

        #opening attachment
        attachment = open(image_loc, "rb") 

        # instance of MIMEBase and named as p 
        p = MIMEBase('application', 'octet-stream') 
  
        # To change the payload into encoded form 
        p.set_payload((attachment).read()) 
  
        # encode into base64 
        encoders.encode_base64(p) 

        #attachment
        p.add_header('Content-Disposition', "attachment; filename= %s" % attachment_name) 

        #attaching image to message
        self.message.attach(p)



    '''
        This function is used to send mail 

    '''

    def send(self):
        # creates SMTP session 
        s = smtplib.SMTP('smtp.gmail.com', 587) 
  
        # start TLS for security 
        s.starttls() 
  
        # Authentication 
        s.login(self.email_id, self.password) 
  
        # Converts the Multipart msg into a string 
        text = self.message.as_string() 
  
        # sending the mail 
        s.sendmail(self.email_id, self.message['To'], text) 
  
        # terminating the session 
        s.quit() 


        


if __name__ == "__main__":

    s = SendMail()              #instance for send mail

    s.to_email('reciever@gmail.com')                    #recievers email id

     
    subject = 'subject of email '                       #this variable holds subject of email
    message = 'message to send through email'           #message to sent through email

    s.write_message("subject", 'message')               #write message


    # attach given image to your email.
    # first argument contains address of image to attach (eg.  ./beach.jpg )
    # second argument contais name of image (eg. 'beach.jpg')

    s.attach('./example.jpg', 'example.jpg')                    # comment this line if you dont want to attach any attachment to email.

    # send email
    s.send()







    






    

    
