from twilio.rest import Client

account = "example"
token = "example"
# found on https://www.twilio.com/console
client = Client(account, token)

message = client.messages.create(to="+12345678910", from_="+12345678910",
                                 body="Hello from Python!")
#sensitive information has been changed 