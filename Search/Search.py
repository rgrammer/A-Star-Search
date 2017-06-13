import numpy
import heapq

test_world = [
  ['.', '*', '*', '*', '*', '*', '*'],
  ['.', '*', '*', '*', '*', '*', '*'],
  ['.', '*', '*', '*', '*', '*', '*'],
  ['.', '.', '.', '.', '.', '.', '.'],
  ['*', '*', '*', '*', '*', '*', '.'],
  ['*', '*', '*', '*', '*', '*', '.'],
  ['*', '*', '*', '*', '*', '*', '.'],
]

COSTS = { '.': 1, '*': 3, '^': 5, '~': 7}

MOVES = [(0,-1), (1,0), (0,1), (-1,0)]

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]
    
    def count(self):
        try:
            return self._index
        except IndexError:
            return -1
        
    def a_star_search( self, world, costs, start, goal, moves):
        frontier = PriorityQueue()
        frontier.push(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0
    
        while frontier.count() > 0:
            current = frontier.pop()
            if current == goal:
                break
            
            for move in MOVES:
                next_point_coordinates = numpy.add(current, move)
                next_point = next_point_coordinates[0], next_point_coordinates[1]
                if next_point[1] >= 0 and next_point[0] >= 0 and next_point[1] <= len(world)-1 and next_point[0] <= len(world[0])-1:
                    terrain = world[next_point[1]][next_point[0]]
                    new_cost = COSTS.get(terrain)
                    if (next_point not in cost_so_far or new_cost < cost_so_far[next_point]) and terrain != "x" :
                        cost_so_far[next_point] = new_cost
                        priority = new_cost + heuristic(goal, next_point)
                        frontier.push(next_point, priority)
                        came_from[next_point] = current
    
        path = []
        path.append(goal)
        i = 1
        while came_from[path[i-1]] != start:
            path.append(came_from[path[i-1]])
            i += 1
        
        print(path) 
    
    test_path = a_star_search( test_world, COSTS, (0, 0), (6, 6), MOVES)