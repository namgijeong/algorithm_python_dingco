# def find_max_plus_or_multiply(array):
#     #0,1 이 나오면 다음번에는 무조건 +
#     #부호 개수는 array -1
#
#     total = 0
#     mark_array = ['.'] * (len(array)-1+len(array))
#
#     for i in range(len(array)):
#         if i != (len(array)-1):
#             if array[i] == 1 or array[i] == 0:
#                 if i == 0:
#                     mark_array[i+1] = '+'
#                 else:
#                     mark_array[(i*2)+1] = '+'
#             else:
#                 if i == 0:
#                     mark_array[i+1] = '*'
#                 else:
#                     mark_array[(i*2)+1] = '*'
#
#     print(mark_array)
#
#     for m in range(len(mark_array)):
#         if mark_array[m] == '+':
#             total += array[m-1]+array[m]
#         else:
#             total *= array[m-1]*array[m]
#
#     print(array)
#
#     return total


def find_max_plus_or_multiply(array):
    #현재 맞닥뜨리는 수가 0이나 1이면 더한다
    #하지만 현재까지의 합계가 1이하이면 나오는 수가 커도 더한다
    plus_or_multiply_sum = 0
    for number in array:
        if number <=1 or plus_or_multiply_sum <=1:
            plus_or_multiply_sum += number
        else:
            plus_or_multiply_sum *= number

    return plus_or_multiply_sum


result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))