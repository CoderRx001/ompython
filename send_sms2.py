from twilio.rest import Client

def send_txt(message):
    account = "example"
    token = "example"
    # found on https://www.twilio.com/console
    client = Client(account, token)
    message = client.messages.create(to="+12345678910", from_="+12345678910", body=message)

send_txt("test message")
#sensitive information has been changed 