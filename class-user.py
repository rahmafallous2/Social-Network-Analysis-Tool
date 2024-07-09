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
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None
        self.size = 0

    def addNode(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def displayNodes(self, name):
        nodes = []
        temp = self.head
        while temp:
            nodes.append((temp.data, name[temp.data]))
            temp = temp.next
        return nodes

    def removeNode(self, target):
        current = self.head
        prev = None
        while current is not None:
            if current.data == target:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self.size -= 1
                return True
            prev = current
            current = current.next
        return False   
class Graph:
    def __init__(self):
        self.AL = {}
        self.name = {}
        self.next_id = 1   
    def addVertex(self, name):
        user = User(self.next_id, name, None, None, None, [])
        if user.id not in self.AL:
            self.AL[user.id] = LL()
            self.name[user.id] = user.name
            self.next_id += 1
            return f"{user.name} (ID: {user.id}) has been added!"
        else:
            return f"{user.name} (ID: {user.id}) already exists!" 
    def removeVertex(self, id):
        if id in self.AL:
            # Remove the user from all adjacency lists
            for key in self.AL:
                self.AL[key].removeNode(id)
            del self.AL[id]
            del self.name[id]
            return f"User with ID {id} has been removed!"
        else:
            return f"User with ID {id} does not exist!"

          

