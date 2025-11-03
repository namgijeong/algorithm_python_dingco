input = [4, 6, 2, 9, 1]

#내 풀이 
# def insertion_sort(array):
#     # 이 부분을 채워보세요!
#     n = len(array)
#     for i in range(1, n):
#         insert_index = i
#         print("i: ",i)
#         for j in range(i-1, -1, -1):
#             print("j: ", j)
#             if array[j] > array[insert_index]:
#                 array[j], array[insert_index] = array[insert_index], array[j]
#                 insert_index = j
#             else:
#                 break
#
#     return array


#강의 풀이
#    1   => 0과 비교
#[4, 6, 2, 9, 1]

#    1  2   => 2는 1, 1은 0과 비교
#[4, 6, 2, 9, 1]

#j의 값
# 1 -> 2,1 -> 3,2,1
#for i in range(1,5):
#    for j in range(i):
#       i=1 , j=0
#       i=2 , j=0
#       i - j

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i-j] < array[i-j-1]:
                array[i - j - 1], array[i-j] = array[i-j], array[i - j - 1]
            else:
                break
    return array

insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))