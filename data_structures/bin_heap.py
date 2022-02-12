class BinaryHeap:

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
    
    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2
    
    def insert(self, value):
        self.heap_list.append(value)
        self.current_size += 1
        self.percolate_up(self.current_size)

    def percolate_down(self, i):
        while (i * 2) <= self.current_size:
            min_child_idx = self.min_child(i)
            if self.heap_list[i] > self.heap_list[min_child_idx]:
                self.heap_list[i], self.heap_list[min_child_idx] = self.heap_list[min_child_idx], self.heap_list[i]
            i = min_child_idx

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def extract_min(self):
        min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.percolate_down(1)
        return min_val

    def heapify(self, arr):
        i = len(arr) // 2
        self.current_size = len(arr)
        self.heap_list = [0] + arr[:]
        while i > 0:
            self.percolate_down(i)
            i -= 1


class PriorityQueue(BinaryHeap):

    def __init__(self):
        self.heap = [(0, None)] # (priority, value)
        self.current_size = 0

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i][0] < self.heap_list[i // 2][0]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2

    def percolate_down(self, i):
        while (i * 2) <= self.current_size:
            min_child_idx = self.min_child(i)
            if self.heap_list[i][0] > self.heap_list[min_child_idx][0]:
                self.heap_list[i], self.heap_list[min_child_idx] = self.heap_list[min_child_idx], self.heap_list[i]
            i = min_child_idx

    def insert(self, priority, value):
        self.heap.append((priority, value))
        self.current_size += 1
        self.percolate_up(self.current_size)

    def heapify(self, arr):
        i = len(arr) // 2
        self.current_size = len(arr)
        heap_list = [(vx.get_distance(), vx) for vx in arr]
        self.heap = [(0, None)] + heap_list[:]
        while i > 0:
            self.percolate_down(i)
            i -= 1

    def extract_min(self):
        min_val = self.heap_list[1][0]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.percolate_down(1)
        return min_val

    def change_priority(self, vx, new_priority):
        for i in range(1, self.current_size + 1):
            if self.heap_list[i][1] == vx:
                self.heap_list[i] = (new_priority, vx)
                self.percolate_up(i)
                self.percolate_down(i)
                break
