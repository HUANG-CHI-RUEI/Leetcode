# https://www.youtube.com/watch?v=efNHPr1PHmM&ab_channel=HappyCoding

# https://www.cnblogs.com/grandyang/p/5558033.html

# Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.

# The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

# You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.

# Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.

# When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

class SnakeGame:

    def __init__(slef, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.queue = collections.deque([0, 0])
        self.score = 0
    
    def move(self, direction: str) -> int:
        head_r, head_c = self.queue[-1] # rightmost

        if direction == 'U':
            head_r -=1
        elif direction =='L':
            head_c -= 1
        elif direction == 'R':
            head_c += 1
        elif direction == 'D':
            head_r += 1

        if head_r < 0 or head_r > self.height - 1 or head_c < 0 or head_c > self.width - 1:
            return -1

        if self.food and [head_r, head_c] == self.food[0]:
            self.queue.append([head_r, head_c])
            self.food.pop(0)
            self.score += 1
        else:
            self.queue.popleft() # which mean snake move see video 17:00

            if [head_r, head_c] in self.queue: # eat itself
                return -1
            else:
                self.queue.append([head_r, head_c])

        return self.score