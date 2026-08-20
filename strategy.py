class CreditCardPayment:
    def pay(self, amount):
        print(f"Kredi kartı ile {amount} TL ödendi.")


class CashPayment:
    def pay(self, amount):
        print(f"Nakit ile {amount} TL ödendi.")


class Payment:
    def __init__(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)


payment = Payment(CreditCardPayment())
payment.pay(100)

payment = Payment(CashPayment())
payment.pay(100)