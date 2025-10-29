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
        #내풀이
        # cur = self.head
        # for i in range(index):
        #     cur = cur.next
        #
        # return cur

        # 강의 풀이
        cur = self.head
        cur_index = 0

        while cur_index != index:
            cur = cur.next
            cur_index += 1

        return cur

    def add_node(self, index, value):
        new_node = Node(value)

        #index 0일때는 어떻게 될까?
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        cur = self.get_node(index-1)
        new_next = cur.next
        new_node.next = new_next
        cur.next = new_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return

        cur = self.get_node(index-1)
        cur.next = cur.next.next
        return

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.add_node(1,6)
linked_list.add_node(0,7)
linked_list.print_all()
print("-----------------------")
linked_list.delete_node(1)
linked_list.print_all()