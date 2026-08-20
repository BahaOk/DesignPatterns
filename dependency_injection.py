class EmailService:

    def send(self):
        print("Email gönderildi.")


class UserService:

    def __init__(self, notification_service):
        self.notification_service = notification_service

    def notify(self):
        self.notification_service.send()


email_service = EmailService()

user_service = UserService(email_service)

user_service.notify()