class Channel:
    def __init__(self):
        self.subscribers = []

    def subscribe(self,user):
        self.subscribers.append(user)

    def upload_video(self,title):
        print(f"Uploaded: {title}")
        for sub in self.subscribers:
            sub.notify(title) 

class Subscriber:
    def __init__(self, name):
        self.name = name

    def notify(self, title):
        print(f"{self.name} received notification for: {title}")

tech_channel = Channel()
alice = Subscriber("Alice")
bob = Subscriber("Bob")

tech_channel.subscribe(alice)
tech_channel.subscribe(bob)

tech_channel.upload_video("Design Patterns Made Easy")        
