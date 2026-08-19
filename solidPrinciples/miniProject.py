from abc import abstractmethod,ABC


# SINGLE RESPONSIBILITY PRINCIPLE - one class,one job
class Order:
    def __init__(self, order_id, customer_name, amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.amount = amount

    def get_summary(self):
        return f"Order_Id : {self.order_id}, Customer_Name : {self.customer_name} & Amount : {self.amount}"


# DEPENDENCY INVERSION PRINCIPLE - no hardcode for one thing
class PaymentGateway(ABC):
    @abstractmethod
    def charge(self, amount):
        pass

# OPEN/CLOSED PRINCIPLE - extent the classes by inheritence
class CreditCardGateway(PaymentGateway):
    def charge(self, amount):
        print(f"Charged ${amount} to Credit Card")


class PayPalGateway(PaymentGateway):
    def charge(self, amount):
        print(f"Charged ${amount} via PayPal")


class FakePaymentGateway(PaymentGateway): 
    def charge(self, amount):
        print(f"[TEST MODE] Pretending to charge ${amount}")       


# INTERFACE SEGREGATION PRINCIPLE - make different classes and use them to inheritate appropriate subclass
class EmailCapable(ABC):
    @abstractmethod
    def send_email(self, message):
        pass

class SMSCapable(ABC):
    @abstractmethod
    def send_sms(self, message):
        pass


class EmailNotifier(EmailCapable):
    def send_email(self, message):
        print(f"Email sent: {message}")


class SMSNotifier(SMSCapable):
    def send_sms(self, message):
        print(f"SMS sent: {message}")   


class MultiChannelNotifier(EmailCapable, SMSCapable):
    def send_email(self, message):
        print(f"[Multi] Email sent: {message}")
    def send_sms(self, message):
        print(f"[Multi] SMS sent: {message}")


class OrderProcessor:
    def __init__(self, payment_gateway: PaymentGateway, notifier):
        self.payment_gateway = payment_gateway   
        self.notifier = notifier

    def process(self, order: Order):
        print(order.get_summary())
        self.payment_gateway.charge(order.amount)  

        if isinstance(self.notifier, EmailCapable):
            self.notifier.send_email(f"Order #{order.order_id} confirmed!")
        if isinstance(self.notifier, SMSCapable):
            self.notifier.send_sms(f"Order #{order.order_id} confirmed!")  


order1 = Order(101, "Aman", 250)
processor1 = OrderProcessor(CreditCardGateway(), EmailNotifier())
processor1.process(order1)

print()

order2 = Order(102, "Riya", 90)
processor2 = OrderProcessor(PayPalGateway(), MultiChannelNotifier())
processor2.process(order2)

print()


order3 = Order(103, "TestUser", 500)
test_processor = OrderProcessor(FakePaymentGateway(), SMSNotifier())
test_processor.process(order3)                                



      
