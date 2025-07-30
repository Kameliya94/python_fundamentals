class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


list_of_emails = []

while (command:= input()) != "Stop":
    sender_, receiver_, content_ = command.split()
    email = Email(sender_, receiver_, content_)
    list_of_emails.append(email)


indices = list(map(int, input().split(", ")))

for index in indices:
    list_of_emails[index].send()

for email in list_of_emails:
    print(email.get_info())



