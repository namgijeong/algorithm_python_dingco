shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus.sort()
    print(menus)
    orders.sort()
    print(orders)
    for i in range(len(orders)):
        search_index = len(menus) // 2
        min_index = 0
        max_index = len(menus) - 1
        while min_index <= max_index:
            if menus[search_index] == orders[i]:
                break
            elif menus[search_index] > orders[i]:
                max_index = search_index - 1
                search_index = (min_index + max_index) // 2
            else:
                min_index = search_index + 1
                search_index = (min_index + max_index) // 2

        if min_index > max_index:
            return False


    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)