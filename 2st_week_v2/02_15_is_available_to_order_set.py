shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus_set = set(menus)
    print(menus_set)
    #set에서는 바로 원소가 들어있는지 아닌지 검사 가능 => 해쉬 테이블

    for order in orders:
        if order not in menus_set:
            return False
    return True


def is_existing_target_number_binary(target, array):
    max_index = len(array) - 1
    min_index = 0
    target_index = (max_index + min_index) // 2

    find_count = 0

    while min_index <= max_index :
        find_count += 1
        if target == array[target_index]:
            print(find_count)
            return True
        elif target > array[target_index]:
            min_index = target_index + 1
            target_index = (max_index + min_index) // 2
        else:
            max_index = target_index - 1
            target_index = (max_index + min_index) // 2
    return False

result = is_available_to_order(shop_menus, shop_orders)
print(result)