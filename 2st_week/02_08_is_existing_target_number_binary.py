finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


#내 풀이
# def is_existing_target_number_binary(target, array):
#     mid_index = (len(array) - 1) // 2
#     mid_number = array[mid_index]
#     max_index = len(array) - 1
#     min_index = 0
#
#     while (min_index <= max_index):
#         if (mid_number < target):
#             min_index = mid_index + 1
#             mid_index = (max_index - min_index) // 2 + min_index
#             mid_number = array[mid_index]
#         elif mid_number == target:
#             return True
#         else:
#             max_index = mid_index - 1
#             mid_index = (max_index - min_index) // 2 + min_index
#             mid_number = array[mid_index]
#
#     return False


#강의 풀이
# 1 ~N
# 1...N/2
# 1.. N/4
# 1 .. N/8
# 1... N/2^k
#k번 탐색하면 N/2^k 개가 남는다
#N/2^k -> 1 가 되려면
#N = 2^k
#log_2(N) = k
#O(log_2(N)) => O(log(N))
#연산량이 반으로 나뉘면 log(N)이라 생각하면 된다

def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    find_count = 0

    while current_min <= current_max:
        find_count += 1
        if array[current_guess] == target:
            print("find count", find_count)
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)