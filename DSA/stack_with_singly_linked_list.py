from DSA.linked_list import LinkedList


class Stack(LinkedList):

    def __init__(self):
        self.ll = LinkedList()
        self.top_element = None

    def push(self, data):
        self.ll.push_front(data)
        self.top_element = self.top()

    def pop(self):
        deleted_data = self.ll.pop_front()
        self.top_element = self.top()
        return deleted_data

    def top(self):
        if self.ll.head is not None:
            self.top_element = self.ll.head.value
        else:
            self.top_element = None
        # print("Top element is:", self.top_element)
        return self.top_element

    def empty(self):
        is_empty = False
        if self.top_element is None:
            print("Stack is empty")
            is_empty = True
        else:
            print("Stack is not empty")
        return is_empty


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.top()
    stack.push(2)
    stack.top()
    stack.push(3)
    stack.top()
    stack.pop()
    stack.top()
    stack.empty()
    stack.pop()
    stack.pop()
    stack.empty()
