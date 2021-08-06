class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, data):
        print("Pushed Front: ", data)
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = self.head

    def pop_front(self):
        if self.head is None:
            raise ValueError("No items in the Linked List")

        deleted_key = self.head.value
        self.head = self.head.next

        if self.tail is None:
            self.tail = self.head
        print("Popped Front: ", deleted_key)
        return deleted_key

    def push_back(self, data):
        print("Pushed Back: ", data)
        new_node = Node(data)

        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop_back(self):
        if self.head is None:
            raise ValueError("No items in the linked list")
        if self.head == self.tail:
            deleted_key = self.head.value
            self.head = self.tail = None
        else:
            temp_node = self.head
            # temp_node.next.next will be None for the last but one element
            while temp_node.next.next is not None:
                temp_node = temp_node.next

            deleted_key = temp_node.next.value
            temp_node.next = None
            self.tail = temp_node
        print("Popped Back: ", deleted_key)
        return deleted_key

    def add_after(self, node, data):
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node

        if self.tail == node:
            self.tail = new_node
        print("Added: ", data, "after node: ", node.value)

    def get_nth_node(self, n):
        temp_node = self.head
        index = 1
        while temp_node is not None:
            if index == n:
                return temp_node
            temp_node = temp_node.next
            index = index + 1

        raise ValueError("No node found at index: ", n)


if __name__ == "__main__":

    # Linked List
    ll = LinkedList()
    # Push front operation
    ll.push_front(1)
    ll.push_front(2)
    ll.push_front(3)
    ll.push_front(4)
    ll.push_front(5)

    ll.pop_front()
    ll.pop_front()
    ll.pop_front()
    ll.pop_front()
    ll.pop_front()

    # Push back operation
    ll.push_back(1)
    ll.push_back(2)
    ll.push_back(3)
    ll.push_back(5)
    ll.push_back(6)
    # Get the 3rd node i.e 3
    node_d = ll.get_nth_node(n=3)
    ll.add_after(node=node_d, data=4)
    node_h = ll.get_nth_node(n=4)

    ll.pop_back()
    ll.pop_back()
    ll.pop_back()
    ll.pop_back()
    ll.pop_back()

