# coding=utf-8
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC6f5db1931e42f95425316546e9449ec7"
# Your Auth Token from twilio.com/console
auth_token  = "3ac3b2a2ad17be8f6d2c457c16fbfabc"
number = "+19282884539"
client = Client(account_sid, auth_token)

message = client.messages.create(to="+8618835109707",from_=number,
    body="由张中俊通过twilio发送")
    
message = client.messages.create(to="+8618636191860",from_=number,
    body="由张中俊通过twilio发送")

print(message.sid)