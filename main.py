class MailItem:
    def __init__(self, sender, receiver, msg):
        self.sender = sender
        self.receiver = receiver
        self.msg = msg
    
    def print(self):
        print("From: " + self.sender)
        print("To: " + self.receiver)
        print("Message: " + self.msg)


class MailServer:
    def __init__(self):
        self.items = []

    def post(self, item):
        self.items.append(item)

    def howManyMailItems(self, who):
        count = 0
        for item in self.items:
            if item.receiver == who:
                count += 1
        return count
    
    def getNextMailItem(self, who):
        foundItem = None

        for item in self.items:
            if item.receiver == who:
                foundItem = item
        
        if foundItem is None:
            pass
        else:
            self.items.remove(foundItem)
        
        return foundItem


class MailClient:
    def __init__(self, server, user):
        self.server = server
        self.user = user
    
    def printNextMailItem(self):
        item = self.server.getNextMailItem(self.user)
        if item is None:
            print("No new mail.")
        else:
            item.print()
    
    def sendMailItem(self, to, msg):
        item = MailItem(self.user, to, msg)
        self.server.post(item)


    
if __name__ == '__main__':
    s = MailServer()
    
    print(" Logging in Joske to mail server...")
    c1 = MailClient(s, "Joske")

    print(" User joske sending mail to Jantje...")
    c1.sendMailItem("Jantje", "Hello!!!")

    print(" Logging in Jantje to mail server...")
    c2 = MailClient(s, "Jantje")

    print(" User Jantje reading mail...")
    c2.printNextMailItem()

    print(" User Jantje reading mail...")
    c2.printNextMailItem()

