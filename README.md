# Amazon Web Scraping Tool

This tool identifies the current price of a product of interest and sends a text to the user if the current price goes below the desired price. 

## Inputs

1. User Agent: Identify and set the user agent for your browser. Google "My User Agent" and edit that on line 12
2. Desired Price: Set the price you want to be notified for on line 16
3. Insert Amazon URL on line 19

## Sending Messages

Messages are sent using Twilios SMS service. Instructions can be found here: https://www.twilio.com/docs/sms/tutorials/how-to-send-sms-messages-python
