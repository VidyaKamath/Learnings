class Node(object):
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, data):
        new_node = Node(data=data)
        print("Pushed Back:", new_node.data)
        if self.tail is None:
            self.head = self.tail = new_node
            new_node.prev = None
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def pop_back(self):
        if self.head is None:
            raise ValueError("No Nodes found")

        if self.head == self.tail:
            deleted_key = self.head.data
            self.head = self.tail = None
        else:
            deleted_key = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
        print("Popped back:", deleted_key)
        return deleted_key

    def add_after_node(self, node, data):
        new_node = Node(data=data)
        new_node.prev = node
        new_node.next = node.next
        node.next = new_node

        if new_node.next is not None:
            new_node.next.prev = new_node

        # if the new_node has to be added after the tail
        # then the new node becomes the tail
        if self.tail == node:
            self.tail = new_node
        print("Added node", data, " after node ", node.data)

    def add_before_node(self, node, data):
        new_node = Node(data=data)
        new_node.next = node
        new_node.prev = node.prev
        node.prev = new_node

        if new_node.prev is not None:
            new_node.prev.next = new_node

        # if the new_node has to be added before the head
        # then the new node becomes the head
        if self.head == node:
            self.head = new_node
        print("Added node", data, " before node ", node.data)

    def get_nth_node(self, n):
        temp_node = self.head
        index = 1

        while temp_node is not None:
            if index == n:
                return temp_node
            index = index + 1
            temp_node = temp_node.next

        raise ValueError("No node found at index:", n)


if __name__ == "__main__":
    dl = DoublyLinkedList()

    dl.push_back(1)
    dl.push_back(3)

    node = dl.get_nth_node(n=1)
    dl.add_after_node(node, 2)
    dl.add_before_node(node, 0)

    dl.pop_back()
    dl.pop_back()
    dl.pop_back()
    dl.pop_back()
