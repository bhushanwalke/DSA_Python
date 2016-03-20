__author__ = 'bhushan'


class MinBinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def __prec_up(self, i):
        while (i/2) > 0:
            if self.heap_list[i] < self.heap_list[i/2]:
                self.heap_list[i], self.heap_list[i/2] = self.heap_list[i/2], self.heap_list[i]
            i = i/2

    def insert(self, new_item):
        self.heap_list.append(new_item)
        self.current_size +=1
        self.__prec_up(self.current_size)


    def __prec_down(self, i):
        while (i*2) <= self.current_size:
            minChild = self.min_child(i)
            if self.heap_list[i] > self.heap_list[minChild]:
                self.heap_list[i], self.heap_list[minChild] = self.heap_list[minChild], self.heap_list[i]
            i = minChild

    def min_child(self, i):
        if (i*2+1)> self.current_size:
            return i*2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                print(self.heap_list[i*2], self.heap_list[i*2+1])
                return i*2
            else:
                return i*2+1

    def del_min(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.__prec_down(1)
        return ret_val


    def build_heap(self, items_list):
        i = len(items_list)/2
        self.current_size = len(items_list)
        self.heap_list = [0] + items_list[:]
        while(i>0):
            self.__prec_down(i)
            i = i - 1

minheap = MinBinHeap()
minheap.build_heap([6,55,4,98])
minheap.insert(5)
minheap.insert(9)
minheap.insert(11)
minheap.insert(14)
minheap.insert(18)
minheap.insert(19)
minheap.insert(21)
minheap.insert(33)
minheap.insert(17)
minheap.insert(27)
print(minheap.heap_list)
print minheap.del_min()

print(minheap.heap_list)

