from cell import Cell
import heapq

class AStar:
    def __init__(self, start, coin):
        self.start = start
        self.coin = coin
        self.open_set = []
        self.closed_set = []
        self.path = []
    def find_shortest_path(self, grid):
        self.open_set.append(self.start)
        self.closed_set.append(self.start)
        self.start.g = 0
        self.start.h = self.start.heuristic(self.coin)
        if self.start.coor() == self.coin.coor():
            return self.start.coor()
        while self.open_set:
            cur_pos = heapq.heappop(self.open_set)
            cur_pos.update_neighbors(grid)
            if cur_pos == self.coin:
                while cur_pos is not None:
                    self.path.append(cur_pos.coor())
                    cur_pos = cur_pos.parent
                return self.path[::-1]
            for i_neighbor in cur_pos.neighbors:
                temp_g = cur_pos.g + 1
                if temp_g < i_neighbor.g:
                    i_neighbor.parent = cur_pos
                    i_neighbor.g = temp_g
                    i_neighbor.h = i_neighbor.heuristic(self.coin)
                    i_neighbor.f = i_neighbor.g + i_neighbor.h
                    if i_neighbor not in self.closed_set:
                        heapq.heappush(self.open_set, i_neighbor)
                        self.closed_set.append(i_neighbor)
                        






