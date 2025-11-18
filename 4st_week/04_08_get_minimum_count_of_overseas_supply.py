# >>> import heapq # heapq 를 사용하기 위해서는 맨 위에 heapq 를 가져온다! 라는 구문을 써주셔야 합니다.
#
# >>> heap = []
# >>> heapq.heappush(heap, 4 * -1)
# >>> heapq.heappush(heap, 1 * -1)
# >>> heapq.heappush(heap, 7 * -1)
# >>> heapq.heappush(heap, 3 * -1)
# >>> print(heap)
# [-7, -3, -4, -1] # 힙의 형태를 유지한채로 원소가 넣어지기 때문에 heap[0]이 최솟값입니다!
#
# >>> print(heapq.heappop(heap) * - 1) # 최댓값을 빼는 방법입니다.
# 7
# >>> print(heap)
# [-4, -3, -1] # 마찬가지로 힙의 형태가 유지됩니다.

import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30

#내 풀이 - 미완성
# def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
#     #총 몇개가 필요한지 구한다
#     #일단 힙에 모든 supplies를 넣는다
#     #dates에 맞닥뜨리면 힙에서 최대를 꺼낸다
#     #그 최대가 dates에 어느 값과 매치하는지를 본다
#     #그 날짜에서 현재날짜를 뺀 값과 그날짜에서 가지고 있게될 밀가루의 양을 계산한다
#     #만약 가지고있게될 밀가루의 양이 0이하면 힙의 다른 값을 뽑는다
#     #아니면 뽑는다.
#
#     current_stock = stock
#     cur_date = 0
#     count = 0
#     heap = []
#     for supply in supplies:
#         heapq.heappush(heap, supply * -1)
#
#     print(heap)
#
#     while cur_date < k and heap:
#         pop_stock = heapq.heappop(heap) * -1
#         pop_stock_index = 0
#         pop_date = 0
#         for i in range(len(supplies)):
#             if supplies[i] == pop_stock:
#                 pop_stock_index = i
#                 pop_date = dates[i]
#                 break
#
#         if pop_date - cur_date - current_stock <= 0 :
#             continue
#         else:
#             current_stock += pop_stock
#             current_stock += (pop_date - cur_date)
#             cur_date += pop_date
#             count += 1
#
#     return count


#강의 풀이
#정렬보다 힙이 좋은 이유
#1. 현재 재고의 상태에 따라 최곳값을 받아야 한다. => 동적 상황
#2. 제일 많은 값만 가져가면 된다.
#-> maxHeap

# while stock <= k : 라는 반복문이 실행될 때 마다 max_heap을 왜 초기화시켜주지 않는 건가요?
# 이전 반복에서 max_heap에 추가된 공급량들 중에서 최댓값이 나올 수 있기 때문에, 새롭게 추가된 공급량들과 비교하여 여전히 가장 큰 값을 가져올 수 있어야 합니다.
# get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40)
# 1. 현재 stock = 4
# 공급 가능 날짜: 4일 → 20 추가
# max_heap = [20]
# 가장 큰 값 20을 사용 → stock = 24
#
# 2.현재 stock = 24
# 공급 가능 날짜: 10일, 15일, 20일 → [5, 10, 5] 추가
# max_heap = [10, 5, 5]
# 가장 큰 값 10을 사용 → stock = 34
#
# 3. 현재 stock = 34
# 공급 가능 날짜 없음
# max_heap = [5, 5]
# 가장 큰 값 5을 사용 → stock = 39
#
# 4.현재 stock = 39
# 공급 가능 날짜 없음
# max_heap = [5]
# 가장 큰 값 5을 사용 → stock = 44 → 목표 달성(k=40)


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    last_added_date_index = 0
    max_heap = []
    while stock < k :
            #후보군이 되어야하는 것들만 넣는다 => 공장이 멈추기 전까지
            while last_added_date_index < len(dates) and dates[last_added_date_index] <= stock:
                heapq.heappush(max_heap, supplies[last_added_date_index] * -1)
                last_added_date_index += 1

            supply = heapq.heappop(max_heap) * -1
            stock += supply
            answer += 1

    return answer

print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))

# 경계값 테스트 케이스들

# 1. stock = k (이미 충분한 경우)
print("정답 = 0 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(10, [5], [20], 10))

# 2. stock = 0 (재고 완전 바닥)
print("정답 = 2 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(0, [0, 10, 15], [20, 10, 15], 35))

# 3. 딱 한 번만 공급받으면 되는 경우
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(5, [5], [30], 30))

# 4. 공급 후 stock이 정확히 k가 되는 경우
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(10, [10], [20], 30))

# 5. 첫날부터 공급 가능한 경우
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(0, [0], [100], 50))

# 6. k = 1 (최소 기간)
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(0, [0], [10], 1))

# 7. 여러 번 공급받아야 하고 딱 맞아떨어지는 경우
print("정답 = 3 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(0, [0, 5, 10], [5, 5, 5], 15))

# 8. 공급 가능 날짜가 여러 개지만 하나만 선택해야 하는 경우
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(5, [5, 6, 7], [100, 10, 10], 50))

# 9. 마지막 날에 공급받는 경우
print("정답 = 2 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(10, [10, 29], [20, 100], 30))

# 10. stock이 k보다 1 작은 경우
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(29, [29], [100], 30))