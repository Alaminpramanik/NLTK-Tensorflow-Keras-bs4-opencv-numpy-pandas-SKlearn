import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('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'))
from_email = Email("poroshpramanik@gmail.com")  # Change to your verified sender
to_email = To("poroshpramanik@gmail.com")  # Change to your recipient
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)

# Get a JSON-ready representation of the Mail object
mail_json = mail.get()

# Send an HTTP POST request to /mail/send
response = sg.client.mail.send.post(request_body=mail_json)
print(response.status_code)
print(response.headers)

# import requests

# requests.post(
#     "https://api.mailgun.net/v3/sandbox2a95526bfb08453d82ece06e5ff4543a.mailgun.org/messages",
#     auth=("api", "69e3e1f73cd66e1d2ecf94c4bc259422-835621cf-87cc358f"),
#     data={"from": "postmaster@sandbox2a95526bfb08453d82ece06e5ff4543a.mailgun.org",
#         "to": 'alamin493641@gmail.com',
#         "subject": "Hello Md Al Amin Pramanik",
#         "text": "Congratulations Md Al Amin Pramanik, you just sent an email with Mailgun!  You are truly awesome!"})

    