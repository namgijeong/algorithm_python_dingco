# Queue 를 실전에서 사용하려면?
# 여러분, 제가 큐를 파이썬에서 사용하기 위해서는 파이썬의 기본 자료형인 list() 를 사용하면 된다고 했었는데, 코딩테스트에서 큐를 사용할 때는
# collections.deque 를 사용하셔야 합니다.
# 성능 차이가 많이 나거든요..! 스택은 그대로 list 사용하셔도 됩니다.
#
# 따라서 앞으로는 큐가 필요할 때 다음과 같이 사용하겠습니다!
# >>> from collections import deque
# >>> queue = deque()
# >>> queue.append(3) # enqueue [3]
# >>> queue.append(4) # enqueue [3] -> [4]
# >>> print(queue.popleft()) # dequeue [4]
# 3


prices = [1, 2, 3, 2, 3]


#내 풀이
# from collections import deque
# def get_price_not_fall_periods(prices):
#     queue = deque()
#     count_list = [0] * len(prices)
#     index = 0
#
#     #큐에 다 넣기
#     for i in range(len(prices)):
#         queue.append(prices[i])
#
#     while queue:
#         price = queue.popleft()
#         count = 0
#         for i in range(len(queue)):
#             count += 1
#             if price > queue[i]:
#                 break
#
#         count_list[index] = count
#         index += 1
#     return count_list


# 강의 풀이 1
# 0 -> 1234
# 1->  234
# 2 -> 34
# 3-> 4
# for i in range(0, 4, 1):
#     for j in range(i+1,5,1)

# def get_price_not_fall_periods(prices):
#     result = [0]*len(prices)
#
#     for i in range(0, len(prices)-1, 1):
#         price_not_fall_period = 0
#         for j in range(i+1,len(prices),1):
#             if prices[i] <= prices[j]:
#                 price_not_fall_period += 1
#             else:
#                 price_not_fall_period += 1
#                 break
#
#         result[i] = price_not_fall_period
#
#     return result


#강의 풀이 2
from collections import deque
def get_price_not_fall_periods(prices):
    result = []
    prices_queue = deque(prices)

    while prices_queue:
        price_not_fall_period = 0
        current_price = prices_queue.popleft()
        for next_price in prices_queue:
            if current_price <= next_price:
                price_not_fall_period += 1
            else:
                price_not_fall_period += 1
                break

        result.append(price_not_fall_period)

    return result

print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))