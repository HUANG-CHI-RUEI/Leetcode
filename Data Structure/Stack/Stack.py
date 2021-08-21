# Stack implementation in python
# https://www.programiz.com/dsa/stack
# push, pop = O(1)


# Creating a stack
def create_stack():
    stack = []
    return stack

# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0

# Adding items into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item:" + item)

# Removing an element from the stack
def pop(stack):
    if (check_empty(stack)):
        return "Stack is empty"
    return stack.pop()

stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))

# class implementation for stack
class Stack(object):
    """docstring for Stack"""
    def __init__(self):
        super(Stack, self).__init__()
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def size(self):
        return len(self.size)

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        if len(self.stack) < 1:
            reutrn "It's empty"
        return "No, the size is {}".format(stack.size())

    def display(self):
        return self.stack

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(2)
print(stack.peek())
print(stack.is_empty())
print(stack.display())
stack.pop()
print(stack.display())
stack.pop()
print(stack.display())
stack.pop()
stack.pop()
print(stack.display())
stack.pop()
print(stack.display())
print(stack.is_empty())