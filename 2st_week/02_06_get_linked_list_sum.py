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

    def get_list_length(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next

        return count

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


#내풀이 => 자릿수가 같은 두수의 맨끝 노드로 이동
# def get_linked_list_sum(linked_list_1, linked_list_2):
#     list1_length = linked_list_1.get_list_length()
#     list2_length = linked_list_2.get_list_length()
#
#     round_flag = 0
#     list1_last = linked_list_1.get_node(list1_length-1).data
#     list2_last = linked_list_2.get_node(list2_length-1).data
#
#     if list1_last + list2_last >= 10:
#         sum_linked_list = LinkedList((list1_last + list2_last)%10)
#         round_flag = 1
#     else:
#         sum_linked_list = LinkedList((list1_last + list2_last))
#
#     for i in range(list1_length-1):
#         sum = linked_list_1.get_node(list1_length-2-i).data + linked_list_2.get_node(list2_length-2-i).data + round_flag
#         if sum >= 10:
#             sum_linked_list.add_node(0, sum % 10)
#             round_flag = 1
#         else:
#             sum_linked_list.add_node(0, sum)
#             round_flag = 0
#
#
#     if round_flag == 1:
#         sum_linked_list.add_node(0, round_flag)
#     return sum_linked_list


#강의 풀이 => 각 리스트마다 아예 십진수 숫자로 변환한후 최종 더하기
#[6] -> [7] -> [8]
#sum_1 = 6
#sum_1 = 6 * 10 +7
#sum_1 = 67 * 0 + 8

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

#강의풀이 출력
print(get_linked_list_sum(linked_list_1, linked_list_2))

#내풀이 출력
# sum_linked_list = get_linked_list_sum(linked_list_1, linked_list_2)
# sum_linked_list.print_all()