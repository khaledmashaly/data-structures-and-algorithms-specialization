# python3
class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def empty(self):
        length = len(self.data)
        if length is 0:
            return True
        else:
            return False


opening_brackets = ['(', '{', '[']
closing_brackets = [')', '}', ']']


def check_match(open_char, close_char):
    return opening_brackets.index(open_char) is closing_brackets.index(close_char)


def is_balanced(code):
    for index, char in enumerate(code):
        char_index = index + 1
        if char in opening_brackets:
            stack.push(char)
            indices.push(char_index)
        elif char in closing_brackets:
            if stack.empty():
                print(char_index)
                break
            else:
                pop_char = stack.pop()
                indices.pop() # remove index of pop'd char
                if check_match(pop_char, char):
                    continue
                else:
                    print(char_index)
                    break
    else:
        if stack.empty():
            print('Success')
        else:
            print(indices.data[0])


s = input()
stack = Stack()
indices = Stack()
is_balanced(s)
