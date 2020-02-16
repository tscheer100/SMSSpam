# PLEASE VIEW THE README BEFORE RUNNING THIS SCRIPT
import json
import smtplib

with open("vars.json", 'r') as log:
    data = json.load(log)

# sets variables to json file
user = data["username"]
password = data["password"]
number = data["number"]
carrier = data["carrier"]
text = data["text"]
repeat = data["repeat"]

# sets carrier list with corresponding email
carriers = {
    'att': '@mms.att.net',
    'tmobile': ' @tmomail.net',
    'verizon': '@vtext.com',
    'sprint': '@page.nextel.com',
    'boost mobile': '@myboostmobile.com',
    'cricket': '@sms.mycricket.com',
    'metroPCS': '@mymetropcs.com',
    'tracfone': '@mmst5.tracfone.com',
    'US cellular': '@email.uscc.net',
    'virgin': '@vmobl.com'
}


def send(message):
    # Set the victim's number
    to_number = number + '{}'.format(carriers[carrier])
    auth = (user, password)

    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])

    # Send text message through SMS gateway of destination number
    server.sendmail(auth[0], to_number, message)


# if statement prevents over-spam
if repeat <= 500:
    for i in range(repeat):
        send(text)
