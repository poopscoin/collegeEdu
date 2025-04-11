from abc import ABC, abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailSender(MessageSender):
    def send(self, message):
        print(f"Надіслано лист: {message}")

class Notification:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def notify(self, message):
        self.sender.send(message)

email_sender = EmailSender()
notifier = Notification(email_sender)
notifier.notify("Привіт!")