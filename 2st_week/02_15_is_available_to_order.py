shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

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

#내 풀이
# def is_available_to_order(menus, orders):
#     menus.sort()
#     orders.sort()
#     print(menus)
#     print(orders)
#
#     available_count = 0
#     orders_length = len(orders)
#     menus_length = len(menus)
#     orders_linked_list = LinkedList(orders[0])
#     menus_linked_list = LinkedList(menus[0])
#
#     for i in range(1, orders_length):
#         orders_linked_list.append(orders[i])
#
#     for i in range(1, menus_length):
#         menus_linked_list.append(menus[i])
#
#     orders_cur = orders_linked_list.head
#     menus_cur = menus_linked_list.head
#
#     while orders_cur is not None and menus_cur is not None:
#         if menus_cur.data == orders_cur.data:
#             menus_cur = menus_cur.next
#             orders_cur = orders_cur.next
#             available_count += 1
#         else:
#             menus_cur = menus_cur.next
#
#     if available_count == orders_length:
#         return True
#     else:
#         return False



#강의 풀이
#이진 탐색
def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2
    find_count = 0

    while current_min <= current_max:
        find_count += 1
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2

    return False


def is_available_to_order(menus, orders):
    # O(NlogN) + O(M) * O(logN)
    menus.sort() #메뉴의 길이가 N -> O(NlogN)
    for order in orders: #오더의 길이가 M이라고 한다면 O(M)
        if not is_existing_target_number_binary(order, menus): #O(logN)
            return False

    return True

result = is_available_to_order(shop_menus, shop_orders)
print(result)