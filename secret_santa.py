import random
from twilio.rest import Client

def getParticpants():
    a_file = open("participants.txt")
    participants = {}
    lines = a_file.readlines()
    for line in lines:
        player = line.split(" ")
        participants[player[0]] = player[1]
    return participants

def assignGifters(numberBook):
    matches = {}
    potential = dict(numberBook)
    for name,number in numberBook.items():
        if (len(potential.keys()) == 1) and name in potential.keys():
            return dict()
        giftee = name
        while giftee is name:
            giftee, number = random.choice(list(potential.items())) 
        matches[name] = giftee
        del potential[giftee]
    return matches

def sendMessages(numberBook,matches):  
    for name, giftee in matches.items():
        number = numberBook[name]
        message ="Hey {}! You are getting a gift for {}.".format(name, giftee)
        sendSMS(number, message)
        print(name + " sent!")

def sendSMS(number, santa_message):
    # the following line needs your Twilio Account SID and Auth Token
    client = Client("SID", "AUTH_TOKEN")

    # change the "from_" number to your Twilio number and the "to" number
    # to the phone number you signed up for Twilio with, or upgrade your
    # account to send SMS to any phone number
    client.messages.create(to=number, 
                        from_="+YOUR_NUMBER", 
                        body=santa_message)

numberBook = getParticpants()

matches = dict()
while len(matches) == 0:
    matches = assignGifters(numberBook)

sendMessages(numberBook, matches)

