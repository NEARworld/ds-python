class Node:
    def __init__(self, data, next: None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, index, data):
        if index >= 0:
            new_node = Node(data, None)
            if self.head is None:
                self.head = new_node
            else:
                i = 0
                current = self.head
                prev = current
                while i < index and current.next is not None:
                    prev = current
                    current = current.next
                    i += 1
                prev.next = new_node
                new_node.next = current.next


linkedList = SinglyLinkedList()
linkedList.insert(0, 10)
linkedList.insert(1, 20)
linkedList.insert(2, 30)
linkedList.insert(3, 40)

linkedList.insert(1, 100)

print(linkedList.head.next.data)