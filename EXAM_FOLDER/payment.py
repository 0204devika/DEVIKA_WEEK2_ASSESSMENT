class Payment:
    def process_payment(self):
        pass
class CreditCardPayment(Payment):
    def process_payment(self):
        print(f"Processing credit card payment")
class PayPalPayment(Payment):
    def process_payment(self):
        print(f"Processing paypal payment")
class bitCoinPayment(Payment):
    def process_payment(self):
        print(f"Processing bitcoin payment")
c=CreditCardPayment()
c.process_payment()
p=PayPalPayment()
p.process_payment()
b=bitCoinPayment()
b.process_payment()
