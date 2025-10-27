input = "011110"
# 0이 1로 변할 때 뒤집는다 => 1을 뒤집어 버리겠다 (1을 만난 시점에 뒤집겠다) -> 전체를 0으로 만들기 위한 작업
#1에서 0으로 될 때 뒤집겠다 -> 0을 만난 시점에 뒤집겠다 -> 전체를 1로 만들기 위한 작업
#i가 0일때, 0번째 인덱스와 1번째 인덱스 => 1번째 인덱스를 기준으로 결정하게 됨
# => 하지만 맨 처음수를 뒤집는거에 대한 계산이 안됨
# => 맨앞자리수를 보고 뒤집는 여부 판단
#i가 1일때, 1번째 인덱스와 2번째 인덱스
#i가 4일때, 4번째 인덱스와 5번째 인덱스


# 내 하다만 풀이
# def find_count_to_turn_out_to_all_zero_or_all_one(string):
#     start_flag_list = []
#     end_flag_list = []
#     count_flag = 0
#     start_flag_list.append(0)
#     for i in range(len(string)-1):
#         if string[i] != string[i+1]:
#             count_flag += 1
#             if count_flag % 2 == 1:
#                 end_flag_list.append(i)
#                 start_flag_list.append(i+1)
#             else:
#                 end_flag_list.append(i)
#                 start_flag_list.append(i + 1)
#     return 1


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string) - 1):  # i=> 0 부터 문자열의 길이 -2:
        if string[i] != string[i+1]:
            if string[i+1] == "1":
                count_to_all_zero += 1
            if string[i+1] == "0":
                count_to_all_one += 1

    print(count_to_all_zero, count_to_all_one)

    return min(count_to_all_zero, count_to_all_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)