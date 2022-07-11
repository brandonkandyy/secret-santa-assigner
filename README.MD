# Secret Santa Assigner
This is a quick program I whipped up to assign people for my annual Secret Santa with my friends that texts them who they are getting a gift for. We wanted to be able to assign people without one person knowing who everyone got or having to get a third party to do it for us. 

# Twilio Dependency
This application uses a service callled [Twilio](https://www.twilio.com/) to send out text messages to the particpants. You must buy a number there aswell as add funds to the number to send messages.  

Add it to the project by running:
`pip install twilio`

# Particpants.txt
This is where you list out . It follows the format of name of the particpant, single space, particpant's phone number:

`NAME +PHONE_NUMBER`

Every particpant is seperatted by a new line

For example:
```
Brandon +123-456-7890

Danny +098-765-4321

Steve +111-222-3333
```
# Quality of Life Improvements
As I said this was made quickly for me and my friends, and since it works for that I have no plans to make this easier for general use. If I did, a few things I would change would be:
- Add JSON config to set Twilio Information aswell as well things like the content of the message
- Put participants into a JSON instead .txt file, this would be easier to read as well as support more than just first name
- Switch around code to use Phone Number as the key instead of Name to support groups that have people with the same name