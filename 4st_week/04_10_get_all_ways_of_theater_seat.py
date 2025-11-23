seat_count = 9
vip_seat_array = [4, 7]

# memo = {
# }

import random

#내 풀이- 미완성
# def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
#     remain_seat_array = []
#     fixed_count = len(fixed_seat_array)
#
#     for i in range(len(fixed_seat_array)):
#         memo[fixed_seat_array[i]] = fixed_seat_array[i]
#
#     for i in range(1, total_count + 1):
#         if i not in fixed_seat_array and i not in remain_seat_array:
#             remain_seat_array.append(i)
#
#     print(memo)
#     print(remain_seat_array)
#
#     for i in range(len(remain_seat_array)):
#         current_value = remain_seat_array[i]
#         prev_value = current_value - 1
#         next_value = current_value + 1
#
#         random_number = random.randrange(1, 3)
#         if random_number == 1:
#             if current_value in memo:
#                 if prev_value in memo and prev_value >= 1:
#                     memo[next_value] = current_value
#                 elif next_value in memo and next_value <= total_count:
#                     memo[prev_value] = current_value
#             else:
#                 memo[current_value] = current_value
#
#         elif random_number == 2:
#             if current_value in memo:
#                 if prev_value in memo and prev_value >= 1:
#                     memo[next_value] = current_value
#                 elif next_value in memo and next_value <= total_count:
#                     memo[prev_value] = current_value
#             else:
#                 memo[prev_value] = current_value
#         else:
#             if current_value in memo:
#                 if prev_value in memo and prev_value >= 1:
#                     memo[next_value] = current_value
#                 elif next_value in memo and next_value <= total_count:
#                     memo[prev_value] = current_value
#             else:
#                 memo[next_value] = current_value
#
#
#     return memo

#강의 풀이
# 123 4 56 7 89
# #1. 숫자를 써보면서 발견해보기
# [1,2] -> [1,2] [2,1] => 2
# [1,2,3] -> [1,2,3] [2,1,3] [1,3,2] =>3
# [1,2,3,4] -> [1,2,3,4] [1,2,4,3] [1,3,2,4] [2,1,3,4] [2,1,4,3] =>5
# [1,2,3,4,5] -> [1,2,3,4,5] [1,2,3,5,4] [2,1,3,4,5] [2,1,3,5,4] [1,2,4,3,5] [2,1,4,3,5] [2,1,3,4,5] [1,3,2,4,5] => 8
# 1 2 3 5 8  => 피보나치 수열

#2 점화식을 통해 파악
# 좌석이 n개만큼 있다
# 1 2 3 .... n-2  n-1  n
# n번째 티켓을 가진 사람이 앉을 수 있는 방법
#
# 1.n번째 좌석에 앉거나
# -> 좌석은 n-1개 가 남아있고, 사람도 n-1번째 티켓까지 가진 사람이 있는 상황 => N-1 명의 사람들을 좌석에 배치하는 방법 => F(N-1)
#
# 2.n-1번째 좌석에 앉거나
# n-1번째 티켓을 가진 사람은 n번째 좌석에 앉아야한다
# -> 좌석은 n-2개가 남아있고, 사람도 n-2번째 티켓까지 가진 사람이 있는 상황 => N-2 명의 사람들을 좌석에 배치하는 방법 => F(N-2)
#
# F(N) = F(N-1) + F(N-2)

#즉 고정된 자석빼고 나머지 좌석을 구역별로 쪼개서 구한다
# F(3)  x   F(2)  x   F(2)
# 123   4    56    7   89
# 3* 2*2 = 12

memo = {
    1: 1,
    2: 2
}

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n-1, fibo_memo) + fibo_dynamic_programming(n -2, fibo_memo)
    fibo_memo[n] = nth_fibo

    return nth_fibo

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1
    current_index = 0

    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1

        #맨처음부터 고정좌석까지의 길이
        count_of_ways = fibo_dynamic_programming(fixed_seat_index - current_index,memo)
        all_ways *= count_of_ways

        #고정좌석 이후의 인덱스
        current_index = fixed_seat_index + 1

    #고정좌석들 목록이 끝난후 마지막 좌석까지의 경우의 수를 구해야한다
    count_of_ways = fibo_dynamic_programming(total_count - current_index, memo)
    all_ways *= count_of_ways

    return all_ways

# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))