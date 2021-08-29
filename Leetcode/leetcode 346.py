# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Example:

# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3
# TC:O(1)
# SC(size)

class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.array = []
        self.sum = 0

    def next(self, val):
        self.sum += val
        self.array.append(val)

        if len(self.array) > self.size:
            self.sum -= self.array.pop(0)

        return self.sum / len(self.array)

class MovingAverage:
    def __ init__(self, size):
        self.size = size
        self.queue = []

    def next(self, val):
        size, queue = self.size, self.queue

        currentSum = sum(queue[-size:])

        return currentSum / len(self.queue[-size:])