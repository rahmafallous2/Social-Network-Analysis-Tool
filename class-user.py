#Social Network Analysis Tool Project
#1. Graph Representation:
# I chose adjacency list for sparse graph representation due to the efficiency in memory usage and traversal speed, ideal for graphs with relatively few edges compared to maximum possible connections between users.
class User:
    def __init__(self, id, name, age, email, phone_number, list_friends):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.phone_number = phone_number
        self.list_friends = list_friends
    def addUser(self, user):
        if user.id not in [friend.id for friend in self.list_friends]:
            self.list_friends.append(user)
        else:
            print("The user already is your friend!")
    def removeUser(self, user):
        if user.id in [friend.id for friend in self.list_friends]:
            self.list_friends = [friend for friend in self.list_friends if friend.id != user.id]
        else:
            print("The user already is not your friend!")
    def displayProfile(self):
        print(f"ID: {self.id}\n"
              f"Name: {self.name}\n"
              f"Age: {self.age}\n"
              f"Email: {self.email}\n"
              f"Phone Number: {self.phone_number}\n"
              f"Friends: {', '.join(f'{friend.name} (ID: {friend.id})' for friend in self.list_friends)}") 
             #this function does not work
             

