from __future__ import print_function
import requests
from bs4 import BeautifulSoup
import pickle
import os
from dotenv import load_dotenv
from pathlib import Path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from twilio.rest import Client

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15'}

class Product:
    def __init__(self):
        self.desired_price = 900
        self.name = ''
        self.price = int()
        self.URL = 'https://www.amazon.com/Tamron-28-75mm-Mirrorless-Limited-Warranty/dp/B07CSLM1X8'

    def set_price(self, price):
        self.price = price

    def set_name(self, name):
        self.name = name

def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string())}

def send_message(service, user_id, message):
    # service: an authorized Gmail API service instance.
    # user_id: User's email address. To indicate the authenticated user, the special value "me" can be used.
    # message: Message to be sent.

    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print ('Message Id: %s'), message['id']
        return message
    except errors.HttpError as error:
        print ('An error occurred: %s'), error

def send_email(price, desired_price, product):
    print('Price lower than desired')

def set_path():
    env_path = Path('./Twilio.env')
    load_dotenv(dotenv_path=env_path)

def send_text(message_body):
    set_path()
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']

    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=message_body,
                        from_='+16084717593',
                        to='+18458006688'
                    )

def get_product_info(URL, headers):
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')

    name = soup.find(id='productTitle').get_text().strip()
    price = soup.find(id='priceblock_ourprice').get_text()[1:-3]

    return(int(price), name)

def set_product_info(price, name, product):
    product.set_name(name)
    product.set_price(price)

def compare_price(product):
    if (product.price < product.desired_price):
        message = 'The price for ' + product.name + ' has dropped below $' + str(product.desired_price) + '!' + '\n\n' + ' Find the link here: ' + product.URL
        send_text(message)

def main():
    product = Product()
    price, name = get_product_info(product.URL, headers)
    set_product_info(price, name, product)
    compare_price(product)

if __name__ == "__main__":
    main()