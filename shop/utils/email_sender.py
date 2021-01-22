import requests
from download_projects.settings import EMAIL_SERVICE_ENDPOINT, EMAIL_SENDER_NAME, EMAIL_SENDER_EMAIL, EMAIL_API_KEY
import json


def sendEmail(name, email, subject, htmlContent):
    # payload = {
    #     "sender": {
    #         "name": EMAIL_SENDER_NAME,
    #         "email": EMAIL_SENDER_EMAIL
    #     },
    #     "to": [
    #         {
    #             "email": email,
    #             "name": name
    #         }
    #     ],
    #     "replyTo": {
    #         "email": EMAIL_SENDER_EMAIL,
    #         "name": EMAIL_SENDER_NAME
    #     },
    #     "htmlContent": htmlContent,
    #     "subject": subject
    # }
    #
    # headers = {
    #     "Accept": "application/json",
    #     "Content-Type": "application/json",
    #     "api-key":  EMAIL_API_KEY  }
    #
    # response = requests.request("POST",
    #                             EMAIL_SERVICE_ENDPOINT,
    #                             json=json.dumps(payload),
    #                             headers=headers)

    return requests.post(
        "https://api.mailgun.net/v3/sandbox3532e685bc8e43a1b79ee66f2c107928.mailgun.org/messages",
        auth=("api", "25296c98ed1f3be1469940298e08f8e9-28d78af2-29665932"),
        data={"from": "RajmalPatidar <"+name+"@sandbox3532e685bc8e43a1b79ee66f2c107928.mailgun.org>",
              "to": ["raj.patidar429@gmail.com"],
              "subject": subject,
              "text": htmlContent })

