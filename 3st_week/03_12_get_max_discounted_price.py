shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


#내 풀이
# def get_max_discounted_price(prices, coupons):
#
#     def number_sort(array):
#         length = len(array)
#         for i in range(length-1):
#             min_index = i
#             for j in range(i+1, length):
#                 if array[j] < array[min_index]:
#                     min_index = j
#             array[i], array[min_index] = array[min_index], array[i]
#         return array
#
#     sorted_prices = number_sort(prices)
#     sorted_coupons = number_sort(coupons)
#     print(sorted_prices)
#     print(sorted_coupons)
#
#     total_sum = 0
#     for i in range(len(sorted_prices)):
#         price = sorted_prices[len(sorted_prices)-1-i]
#         if len(sorted_coupons) > 0 and len(sorted_coupons)-1-i >= 0 and sorted_coupons[len(sorted_coupons)-1-i] is not None:
#             total_sum += (100-sorted_coupons[len(sorted_coupons)-1-i])/100 * price
#         else:
#             total_sum += price
#
#     return total_sum


#강의 풀이
def get_max_discounted_price(prices, coupons):
    #내림차순 정렬 => reverse=True
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    price_index = 0
    coupon_index = 0
    max_discounted_price = 0

    while price_index < len(prices) and coupon_index < len(coupons):
        discounted_price = prices[price_index] * (100 - coupons[coupon_index]) / 100
        max_discounted_price += discounted_price
        price_index += 1
        coupon_index += 1

    #쿠폰이 없는 상황
    while price_index < len(prices):
        max_discounted_price += prices[price_index]
        price_index += 1

    return max_discounted_price

print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))