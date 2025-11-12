class MaxHeap:
    def __init__(self):
        self.items = [None]


    #내 풀이
    # def insert(self, value):
    #     current_index = len(self.items)
    #     self.items.append(value)
    #     while current_index != 0:
    #         parent_index = int(current_index / 2)
    #         parent_value = self.items[parent_index]
    #         if parent_value is not None and parent_value < value:
    #             current_index, parent_index = parent_index, current_index
    #             self.items[parent_index] = parent_value
    #             self.items[current_index] = value
    #         else:
    #             break
    #     return self.items


    #강의 풀이
    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1
        
        #1인 경우에는 이미 rootnode라 더 올라갈 일이 없음
        while cur_index != 1 :
            parent_index = cur_index // 2

            if self.items[cur_index] > self.items[parent_index]:
                self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]
                cur_index = parent_index
            else:
                break

max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!