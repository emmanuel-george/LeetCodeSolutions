class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = new_node

    def insert_at_head(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def len_of_ll(self):
        currentNode = self.head
        if self.head is None:
            return 0
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length

    def insert_at(self, new_node, position):
        if position < 0 or position > self.len_of_ll():
            print('Invalid Position')
            return
        if position == 0:
            self.insert_at_head(new_node)
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                new_node.next = previousNode.next
                previousNode.next = new_node
                return
            else:
                previousNode = currentNode
                currentNode = currentNode.next
                currentPosition += 1

    def print_linked_list(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

    def delete_end(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None

    def delete_head(self):
        if self.is_list_empty() is False:
            tempNode = self.head
            self.head = tempNode.next
            del tempNode
        else:
            print('The List is Empty')

    def is_list_empty(self):
        if self.len_of_ll() <= 0:
            return True
        return False

    def delete_node_at_position(self, position):
        if position < 0 or position >= self.len_of_ll():
            print('Invalid Position')
        if self.is_list_empty() is False:
            if position is 0:
                self.delete_head()
                return

        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = currentNode.next
                currentNode.next = None
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1


firstNode = Node('John')
linkedList = LinkedList()
linkedList.insert_end(firstNode)
secondNode = Node('Ben')
linkedList.insert_end(secondNode)
thirdNode = Node('Mathew')
linkedList.insert_end(thirdNode)
# # linkedList.insert_at(Node(50), 1)
# linkedList.delete_end()
linkedList.delete_node_at_position(1)
linkedList.print_linked_list()
