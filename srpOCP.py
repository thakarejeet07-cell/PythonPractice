from abc import ABC , abstractmethod


class NotificationSender(ABC):
    @abstractmethod
    def send(self,message):
        pass

class EmailNotification(NotificationSender):
    def send(self, message):
        print(f"Email sent: {message}")

class SMSNotification(NotificationSender):
    def send(self, message):
        print(f"SMS sent: {message}")


class PushNotification(NotificationSender):
    def send(self, message):
        print(f"Push notification sent: {message}")


class Order:
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

    def get_summary(self):
        return f"Order #{self.order_id}: ${self.amount}"

class OrderProcessor:
    def __init__(self, notifier: NotificationSender):
        self.notifier = notifier

    def process(self, order: Order):
        print(f"Processing {order.get_summary()}")
        self.notifier.send(f"Your order #{order.order_id} has been processed!")


order = Order(101, 250)
processor = OrderProcessor(EmailNotification())
processor.process(order)

# switch to SMS - zero changes to OrderProcessor or Order class
processor2 = OrderProcessor(SMSNotification())
processor2.process(order)        



