from DSA.stack_with_singly_linked_list import Stack

stack = Stack()


def is_balanced(input_str):
    """
    supported parantheses: {}, [] ,()
    :param input_str: {{{][]()}}}
    :return: bool
    """
    open_parantheses = ['{', '[', '(']
    for char in input_str:
        if char in open_parantheses:
            stack.push(char)
        else:
            if stack.empty():
                return False
            else:
                pop_element = stack.pop()
                if (char == '{' and pop_element != '}') or (char == '[' and pop_element != ']') or (
                        char == '(' and pop_element != ')'):
                    return False
    return stack.empty()


if __name__ == "__main__":
    balanced_str = "{{{[]()[(])}}}"
    print(is_balanced(balanced_str))
