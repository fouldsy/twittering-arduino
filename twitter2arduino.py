## Import libraries
import twitter
import serial
import time

## Authenticate with Twitter API
api = twitter.Api(consumer_key='', consumer_secret='', access_token_key='', access_token_secret='') 

## Configure Serial Port
arduino = serial.Serial('/dev/tty.usbmodem3d11', 9600)

## Get twitter mentions, write to array, extract latest
mentions = api.GetMentions()

## Get the contents of the latest message
mentions_content = [s.text for s in mentions]
latest_content = mentions_content[0]

## Discard first 17 characters, which would be "@fouldsy_arduino " for me
## Replace '17' with the number of characters of your username
message = latest_content[17:]

## Determine what the message said, check for lights 'on' or 'off'
## We then need to send the Arduino the appropriate command
if message == "lights on":
	arduino.write("1")
elif message == "lights off":
	arduino.write("2")
	
## If the message wasn't understood, don't send Arduino data
else:
	print "Sorry, unknown request"
