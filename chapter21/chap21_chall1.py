# http://tinyurl.com/j7d7nx2

class Stack() :
    def __init__(self) :
        self.items = []

    def is_empty(self) :
        return not selt.items

    def push(self, item) :
        self.items.append(item)

    def pop(self) :
        return self.items.pop()

    def peek(self) :
        return self.items[-1]

    def size(self) :
        return len(self.items)

stack = Stack()
for letter in "yesterdey" :
    stack.push(letter)

reversed_string = ""

for i in range(len(stack.items)) :
    reversed_string += stack.pop()

print(reversed_string)
