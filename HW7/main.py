class Stack:

    def __init__(self):
        self.elements = []

    def push(self, data):
        self.elements.append(data)

    def pop(self):
        if self.elements:
            return self.elements.pop()
        else:
            return None

    def isEmpty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False

    def peek(self):
        return self.elements[-1]

    def size(self):
        return len(self.elements)


if __name__ == "__main__":

    in_string = str(input('\nВведите строку: '))

    def is_balanced(s):
        pairs = {"{": "}", "(": ")", "[": "]"}
        stack = Stack()
        for el in in_string:
            if el in "{[(":
                stack.push(el)
            elif (not stack.isEmpty()) and (el == pairs[stack.peek()]):
                stack.pop()
            else:
                return 'Несбалансированно'
        if stack.size() == 0:
            return 'Сбалансированно'

    print(is_balanced(in_string))
