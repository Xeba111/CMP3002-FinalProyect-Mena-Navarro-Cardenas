# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Node:

    def __init__(self, val=None):
        self.val = val
        self.next_node = None

    def set_next_node(self, next_node):
        self.next_node = next_node



class Singly_linked_list:

    def __init__(self, head_node=None):
        self.head_node = head_node

    def list_traversed(self):
        node = self.head_node
        i = 0
        out = set()
        out.add(node.val)
        node = node.next_node
        while node.next_node is not self.head_node.next_node:
            out.add(node.val)
            node = node.next_node
            i += 1
        return out

    def delete(self, val):
        node = self.head_node
        prev = None
        while node.val != val:
            prev = node
            node = node.next_node

        if prev:
            prev.next_node = node.next_node
        else:
            self.head_node = node.next_node
        node.next_node = None

    def insertVal(self, new_node):
        node = self.head_node
        while node:
            if node.next_node == self.head_node:
                node.set_next_node(new_node)
                new_node.set_next_node(self.head_node)
                break
            node = node.next_node
        return self.list_traversed()

m1 = Node(1)
m2 = Node(2)
m3 = Node(3)
m4 = Node(4)
m1.set_next_node(m2)
m2.set_next_node(m3)
m3.set_next_node(m4)
m4.set_next_node(m1)
list1 = Singly_linked_list(m1)
m5 =Node(5)

n1 = Node(1)
n2 = Node(4)
n3 = Node(5)
n4 = Node(4)
n1.set_next_node(n2)
n2.set_next_node(n3)
n3.set_next_node(n4)
n4.set_next_node(n1)
list2 = Singly_linked_list(n1)
n5 =Node(9)