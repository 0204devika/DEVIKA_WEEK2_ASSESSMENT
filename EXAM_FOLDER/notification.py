class Notification:
    def __init__(self,message):
        self.message=message
    def send(self):
        print("Sending notification:", self.message)
class EmailNotification(Notification):
    def __init__(self,message,email):
        super().__init__(message)
        self.email=email
    def send(self):
        print("Sending email:", self.email)
class SMSNotification(Notification):
    def __init__(self,message,phone_number):
        super().__init__(message)
        self.phone_number=phone_number
    def send(self):
        print("sending sms to", self.phone_number)
e=EmailNotification("hi, this is message","hello, this is email notification")
e.send()
s=SMSNotification("hello this is message",6281445834)
s.send()
        