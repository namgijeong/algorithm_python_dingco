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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        for i in range(0, index):
            cur = cur.next
        return cur

    #강의 풀이
    # def get_node(self, index):
    #     cur = self.head
    #     cur_index = 0
    #
    #     while cur_index != index:
    #         cur = cur.next
    #         cur_index += 1
    #     return cur

    def add_node(self, index, value):
        cur = self.head
        if index == 0:
            tmp = cur
            self.head = Node(value)
            self.head.next = tmp
            return

        for i in range(0, index-1):
            cur = cur.next
        tmp = cur
        cur = Node(value)
        cur.next = tmp
        return

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0, 3)
print(linked_list.get_node(0)) # -> 5를 들고 있는 노드를 반환해야 합니다!
print(linked_list.get_node(0).data)