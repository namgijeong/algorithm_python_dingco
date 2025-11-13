class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break


    #내 풀이
    # 미완성 => 만약 가장 마지막 레벨인데 인덱스가 마지막 노드가 아닐때도 끝내야하는데.. 이진트리 높이와 상관이 있는데 어떻게하지?
    # def delete(self):
    #     delete_item = self.items[1]
    #     cur_item = self.items[len(self.items) - 1]
    #
    #     #루트노드와 마지막 노드 자리 바꾼다
    #     self.items[1], self.items[len(self.items) - 1] = self.items[len(self.items) - 1], self.items[1]
    #
    #     #마지막 노드 지운다
    #     self.items = self.items[:len(self.items)-1]
    #     print(self.items)
    #
    #     #루트노드에서부터 자식과 비교해서 다시 정렬한다
    #     cur_length = len(self.items)
    #     cur_index = 1
    #     while cur_index < cur_length - 2:
    #         left_index = cur_index * 2
    #         right_index = cur_index * 2 + 1
    #         change_index = left_index
    #         if self.items[left_index] < self.items[right_index]:
    #             change_index = right_index
    #
    #         if self.items[change_index] > self.items[cur_index]:
    #             self.items[change_index], self.items[cur_index] = self.items[cur_index], self.items[change_index]
    #             cur_index = change_index
    #         else:
    #             break
    #         print(cur_index)
    #
    #     return delete_item


    #강의 풀이
    def delete(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        prev_max = self.items.pop()

        cur_index = 1
        while cur_index <= len(self.items) - 1:
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1
            max_index = cur_index

            if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
                max_index = left_child_index

            if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index

            if max_index == cur_index:
                break

            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]
            cur_index = max_index

        return prev_max


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]