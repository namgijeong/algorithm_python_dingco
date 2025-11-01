shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


#강의 풀이 2
#집합 자료형 사용
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
    #O(N) + O(M) * O(1)
    menus_set = set(menus) # O(N)
    for order in orders: #M -> O(M)
        if order not in menus_set: #0(1) => hash table 때문
            return False
    return True
   

result = is_available_to_order(shop_menus, shop_orders)
print(result)