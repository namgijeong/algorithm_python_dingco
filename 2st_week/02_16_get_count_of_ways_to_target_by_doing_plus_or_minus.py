#import random
numbers = [1, 1, 1, 1, 1]
target_number = 3


#내 풀이 풀다만것
# total_sum = 0
# count = 0
# def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
#     global total_sum
#     print(total_sum)
#     if len(array) == 1 and target == total_sum:
#         global count
#         count += 1
#         return count
#
#     if len(array) == 1:
#         return 0
#
#     sum = array[0]
#     if random.randint(1, 2) == 1:
#         total_sum = total_sum + sum
#     else:
#         total_sum = total_sum - sum
#
#     return get_count_of_ways_to_target_by_doing_plus_or_minus(array[1:], target)

#다른 쉬운 예시를 생각해본다
#numbers = [2,3,1]
#target_number = 0
#어떠한 수학적 원리도 없이 모든 경우의 수를 구해야한다
#1. +2 +3 +1 = 6
#2. +2 +3 -1 = 4
#N의 길이의 배열에서 더하거나 뺀 모든 경우의 수는
#N -1 의 길이의 배열에서 마지막 원소를 더하거나 뺀 경우의 수를 추가하면 된다
#모든 경우의 수를 구하는 내부 함수를 새로 만든다
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    all_ways = []

    def get_all_ways_by_doing_plus_or_minus(array, current_index, current_sum):
        if current_index == len(array):
            all_ways.append(current_sum)
            return

        get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index])
        get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index])

    get_all_ways_by_doing_plus_or_minus(array, 0, 0)

    target_count = 0
    for way in all_ways:
        if target == way:
            target_count += 1

    return target_count



print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!
