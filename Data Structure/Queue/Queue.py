# Queue implementation in python
# https://www.programiz.com/dsa/queue
# dequeue , enqueue = O(1). If uese pop(n) in python, might be O(n)

class Queue:
    def __init__(self):
        self.queue = []

    # Add a element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("After removing an element")
q.display()