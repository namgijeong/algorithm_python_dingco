top_heights = [6, 9, 5, 7, 4]

# 실제 코드에서는 파이썬의 list 를 이용해서 스택으로 사용합니다!
# stack = []            # 빈 스택 초기화
# stack.append(4)       # 스택 push(4)
# stack.append(3)       # 스택 push(3)
# top = stack.pop()     # 스택 pop
# print(top)            # 3!


#내 풀이
# def get_receiver_top_orders(heights):
#     #일단 스택에 다 넣기
#     stack = []
#     stack_index = []
#     stack_index_stack = []
#     for i in range(len(heights)):
#         stack.append(heights[i])
#
#     for i in range(len(heights)):
#         cur_tower = stack.pop()
#         index = 0
#         for j in range(len(stack)-1, -1, -1):
#             #print(stack[j], cur_tower)
#             if stack[j] > cur_tower:
#                 index = j + 1
#                 break
#
#         stack_index.append(index)
#
#     for i in range(len(stack_index)):
#         stack_index_stack.append(stack_index[len(stack_index)-1-i])
#
#     return stack_index_stack


#강의 풀이 1
# def get_receiver_top_orders(heights):
#     answer = [0] * len(heights)
#
#     for i in range(len(heights) - 1, 0, -1):
#         for j in range(i-1, -1, -1):
#             if heights[i] < heights[j]:
#                 answer[i] = j + 1
#                 break
#
#     return answer


#강의 풀이 2
def get_receiver_top_orders(heights):
    answer = [0] * len(heights)

    #파이썬의 독특한 문법 => 자료구조가 비어있는지 여부
    while heights:
        height = heights.pop()

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > height:
                answer[len(heights)] = i + 1
                break

    return answer

print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))