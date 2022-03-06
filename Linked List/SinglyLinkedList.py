class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("Previous node is not in the list")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def deleteNode(self, key):
        temp = self.head
        if temp and temp.value == key:
            self.head = temp.next
            temp = None
            return

        while temp:
            if temp.value == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def deleteNodeAtPosition(self, position):
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next
            return self.head
        index = 0
        current = self.head
        prev = self.head
        temp = self.head
        
        while current is not None:
            if index == position:
                prev.next = current.next
                break
            prev = current
            current = current.next
            index += 1
        prev.next = temp
        return prev

if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second

    second.next = third

    # llist.printList()

    llist.append(6)
    llist.push(7)
    llist.append(8)
    llist.insertAfter(llist.head.next, 9)
    # llist.printList()

    llist.deleteNode(3)
    llist.printList()