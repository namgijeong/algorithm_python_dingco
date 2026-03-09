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

#내 풀이 => 이것도 정답
# def get_linked_list_sum(linked_list_1, linked_list_2):
#     cur1 = linked_list_1.head
#     cur2 = linked_list_2.head
#     sum_array = []
#     sum_digit_array = []
#     sum = 0
#     while cur1 is not None:
#             sum_array.append(cur1.data + cur2.data)
#             cur1 = cur1.next
#             cur2 = cur2.next
#
#     print(sum_array)
#     for i in range(len(sum_array)-1, -1, -1):
#         sum_digit_array.append(10**(len(sum_array)-1-i)*sum_array[i])
#         print(10**(len(sum_array)-i)*sum_array[i])
#
#     for i in range(len(sum_digit_array)-1, -1,-1):
#         sum += sum_digit_array[i]
#
#     return sum

#강의풀이
def get_single_linked_list_sum(linked_list):
    sum = 0
    cur = linked_list.head
    while cur is not None:
        sum = sum * 10 + cur.data
        cur = cur.next

    return sum

def get_linked_list_sum(linked_list_1, linked_list_2):
    sum_1 = get_single_linked_list_sum(linked_list_1)
    sum_2 = get_single_linked_list_sum(linked_list_2)

    return sum_1 + sum_2

linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))