# Datetime function has been imported from datetime library.
from datetime import datetime


# Spy class contains all basic info of a spy.
class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


# ChatMessage class contains all chat related info.
class ChatMessage:

    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
# Spy classs has been initialized with some values.
spy = Spy('Alpha', 'Mr.', 24, 3.4)

# Few friends pre-added
friend_one = Spy('Delta', 'Mr.', 27, 3.5)
friend_two = Spy('Charlie', 'Ms.', 23, 3.6)
friend_three = Spy('Tango', 'Mr.', 25, 3.7)

# Friends list contains 3 friends.
friends = [friend_one, friend_two, friend_three]