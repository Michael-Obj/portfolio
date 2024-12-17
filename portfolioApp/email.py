from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
import ssl
import smtplib
from django.template.loader import render_to_string
from django.utils.html import strip_tags


from dotenv import load_dotenv
import os
load_dotenv()



    
# @shared_task
def emailInquiry(receiver:str, subject:str, body:str, obj, name: str=""):
    try:
        email_sender = "michaeloluwole99@gmail.com"
        email_password = os.getenv("EMAIL_PASSWORD")
        email_receiver = receiver

        subject = subject
        
        html_message = render_to_string('email.html', {"name": name, "message": body, "my_variable": obj})
        # html_message = render_to_string('mail_template.html', {'context': 'values'})
        # plain_message = strip_tags(html_message)

        body = f"""{body}"""

        emailObj = MIMEMultipart()
        emailObj['From'] = "Michael Oluwole"
        emailObj['To'] = email_receiver
        emailObj['subject'] = subject
        emailObj.attach(MIMEText(html_message, "html"))
        # emailObj.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, emailObj.as_string())
            return "Notification Successful"
    except Exception as ex:
        return ex
    
    