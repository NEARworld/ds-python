class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, index, data):
        if index >= 0:
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                i = 0
                current = self.head
                prev = current

                while i < index and current is not None:
                    prev = current
                    current = current.next
                    i += 1
                prev.next = new_node
                if current:
                    new_node.next = current.next

    def delete(self, index):
        if self.head is None:
            print("The list is empty")
        else:
            i = 0
            prev = None
            current = self.head
            while index > i and current.next is not None:
                prev = current
                current = current.next
                i += 1
            prev.next = current.next

    def traverse(self):
        if self.head is None:
            print("The list is empty")
        else:
            current = self.head
            while current:
                print(current.data)
                current = current.next


linkedList = SinglyLinkedList()
linkedList.insert(0, 10)
linkedList.insert(1, 20)
linkedList.insert(2, 30)
linkedList.insert(3, 40)

linkedList.insert(1, 100)
#
# print(linkedList.head.next.data)  # 100
# linkedList.delete(1)
# print(linkedList.head.next.next.next.next.next.next.data)  # 30
linkedList.traverse()
