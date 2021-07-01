# BASIC -- https://practice.geeksforgeeks.org/problems/implement-queue-using-linked-list/1


class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

front = None
rear = None
temp1 = None

# Stack
class stack:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, item):
        if self.isEmpty():
            self.head = Node(item)
        else:
            temp = Node(item)
            temp.next = self.head
            self.head = temp

    def pop(self):
        if self.isEmpty():
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return temp.data

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.head.data

# QUEUE actually
class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, item):
        if self.tail == None:
            temp = Node(item)
            self.head = temp
            self.tail = temp
        else:
            temp = Node(item)
            self.tail.next = temp
            self.tail = temp

    def pop(self):
        if self.isEmpty():
            return -1
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return temp.data

qq = MyQueue()
qq.push('1')
qq.push('2')
qq.push('3')
print(qq.pop())

tt = stack()
tt.push('a')
tt.push('b')
tt.push('c')
print(tt.pop())





