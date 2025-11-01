class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    #내풀이
    # def get_kth_node_from_last(self, k):
    #     cur = self.head
    #     #일단 현재 노드의 길이를 구한다
    #     # 길이가 3이면, 2가 매개변수이면 1 인덱스
    #     # 길이가 3이면, 1이 매개변수이면 2가 인덱스
    #     count = 0
    #     while cur is not None:
    #         count = count + 1
    #         cur = cur.next
    #
    #     find_index = count - k
    #     cur = self.head
    #     for index in range(find_index):
    #         cur = cur.next
    #
    #     return cur


    #강의 풀이
    # def get_kth_node_from_last(self, k):
    #     cur = self.head
    #     length = 1
    #     while cur.next is not None:
    #         cur = cur.next
    #         length += 1
    #
    #     end_length = length - k
    #     cur = self.head
    #
    #     for i in range(end_length):
    #         cur = cur.next
    #
    #     return cur


#강의 풀이2
    #끝에서부터 k만큼 떨어져있는 노드를 한번의 순회만에 구한다
    #k만큼 떨어진 두 노드를 순차적으로 모두 한칸씩 이동시킨다
    #slow          fast
    #       slow          fast
    #              slow          fast
    #                     slow           fast
    #[6] -> [7] -> [8] -> [9] -> [10] -> [11]
    def get_kth_node_from_last(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        #fast가 none일때 k=1일때 slow는 마지막 노드가 될 것이다
        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow
    
linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!