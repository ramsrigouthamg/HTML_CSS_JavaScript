from twilio.rest import TwilioRestClient
#import twilio
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC533f1015b0e190441647ed8e0ff81287"
auth_token  = "2c8d26261821ecd39a9256768686a759"
#client = twilio.rest.TwilioRestClient(account_sid, auth_token)
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hi Ram ! TEST MESSAGE from Ramsri",
    to="+14804526153",    # Replace with your phone number
    from_="+14805265501") # Replace with your Twilio number
print message.sid
