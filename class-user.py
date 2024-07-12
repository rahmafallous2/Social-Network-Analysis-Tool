#Social Network Analysis Tool Project
#1. Graph Representation:
# I chose adjacency list for sparse graph representation due to the efficiency in memory usage and traversal speed, ideal for graphs with relatively few edges compared to maximum possible connections between users.
from collections import deque

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
            print("The user is already your friend!")

    def removeUser(self, user):
        if user.id in [friend.id for friend in self.list_friends]:
            self.list_friends = [friend for friend in self.list_friends if friend.id != user.id]
        else:
            print("The user is not your friend!")

    def displayProfile(self):
        print(f"ID: {self.id}\n"
              f"Name: {self.name}\n"
              f"Age: {self.age}\n"
              f"Email: {self.email}\n"
              f"Phone Number: {self.phone_number}\n"
              f"Friends: {', '.join(f'{friend.name} (ID: {friend.id})' for friend in self.list_friends)}")

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

    def addRelation(self, id1, id2, relation):
        if id1 in self.AL and id2 in self.AL:
            if relation == "Follow":
                self.AL[id1].addNode(id2)
                print(self.name[id1] + " followed " + self.name[id2] + "!")
            elif relation == "Unfollow":
                self.AL[id1].removeNode(id2)
                print(self.name[id1] + " unfollowed " + self.name[id2] + "!")
            else:
                self.AL[id1].addNode(id2)
                self.AL[id2].addNode(id1)
                print("Friendship established between " + self.name[id1] + " and " + self.name[id2] + "!")
        elif id1 not in self.AL and id2 not in self.AL:
            print("Invalid users", id1, "and", id2, "\n")
        elif id1 not in self.AL:
            print("Invalid user", id1, "\n")
        else:
            print("Invalid user", id2, "\n")

    def displayGraph(self):
        if not self.AL:
            print("Graph is empty!\n")
            return
        for user in self.AL:
            print(self.name[user] + ":", end=" ")
            nodes = self.AL[user].displayNodes(self.name)
            print(", ".join([f"{name} (ID: {id})" for id, name in nodes]))

    def BFS(self, starting_vertex):
        visited = [False] * (max(self.AL) + 1)
        queue = deque([starting_vertex])
        visited[starting_vertex] = True

        while queue:
            vertex = queue.popleft()
            print(self.name[vertex], end=" ")

            nodes = self.AL[vertex].displayNodes(self.name)
            for neighbor, _ in nodes:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        print()

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(self.name[v], end=" ")

        nodes = self.AL[v].displayNodes(self.name)
        for neighbor, _ in nodes:
            if neighbor not in visited:
                self.DFSUtil(neighbor, visited)

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)
        print()

    def dijkstra(self, src):
        if src not in self.AL:
            print(f"Vertex {src} not found in the graph.")
            return

        dist = {vertex_id: float('inf') for vertex_id in self.AL}
        dist[src] = 0
        visited = set()

        while len(visited) < len(self.AL):
            min_dist = float('inf')
            min_vertex = None

            for vertex_id in dist:
                if vertex_id not in visited and dist[vertex_id] < min_dist:
                    min_dist = dist[vertex_id]
                    min_vertex = vertex_id

            if min_vertex is None:
                break

            visited.add(min_vertex)

            for neighbor_id, _ in self.AL[min_vertex].displayNodes(self.name):
                distance = dist[min_vertex] + 1  # Assuming unweighted graph, each edge has distance 1
                if distance < dist[neighbor_id]:
                    dist[neighbor_id] = distance

        return dist

    def connectedComponents(self):
        visited = {key: False for key in self.AL}
        cc = []

        for v in self.AL:
            if not visited[v]:
                temp = []
                self.DFSUtil(v, visited, temp)
                cc.append(temp)

        return cc

    def quickSort(self, theSeq):
        self.recQuickSort(theSeq, 0, len(theSeq) - 1)

    def recQuickSort(self, theSeq, first, last):
        if first < last:
            # Partition the sequence and obtain the pivot position
            pivot = self.partitionSeq(theSeq, first, last)
            # Recursively sort the two subsequences
            self.recQuickSort(theSeq, first, pivot - 1)
            self.recQuickSort(theSeq, pivot + 1, last)

    def partitionSeq(self, theSeq, first, last):
        pivot = theSeq[first]
        left = first + 1
        right = last
        done = False
        while not done:
            while left <= right and theSeq[left] <= pivot:
                left = left + 1
            while theSeq[right] >= pivot and right >= left:
                right = right - 1
            if right < left:
                done = True
            else:
                # Swap the elements
                temp = theSeq[first]
                theSeq[first] = theSeq[right]
                theSeq[right] = temp
        # Swap the pivot element with the right element
        temp = theSeq[first]
        theSeq[first] = theSeq[right]
        theSeq[right] = temp
        return right

    def mergeSort(self, seq):
        self.mergeSortRecursively(seq, 0, len(seq))

    def mergeSortRecursively(self, seq, first, last):
        if first < last - 1:
            mid = (first + last) // 2
            self.mergeSortRecursively(seq, first, mid)
            self.mergeSortRecursively(seq, mid, last)
            self.merge(seq, first, mid, last)

    def merge(self, seq, first, mid, last):
        temp = []
        i = first
        j = mid

        while i < mid and j < last:
            if seq[i] < seq[j]:
                temp.append(seq[i])
                i += 1
            else:
                temp.append(seq[j])
                j += 1

        while i < mid:
            temp.append(seq[i])
            i += 1

        while j < last:
            temp.append(seq[j])
            j += 1

        for k in range(len(temp)):
            seq[first + k] = temp[k]
