class Subscriber:

    def update(self, message):
        print(f"Bildirim: {message}")


class Channel:

    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


channel = Channel()

user1 = Subscriber()
user2 = Subscriber()

channel.subscribe(user1)
channel.subscribe(user2)

channel.notify("Yeni video yayınlandı!")