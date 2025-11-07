#내 풀이 )()( 일때는 적용안됨
# def is_correct_parenthesis(string):
#     length = len(string)
#     left_close = False
#     left_close_count = 0
#     right_close = False
#     right_close_count = 0
#
#     #일단 스택에 다 담기
#     stack_close = list(string)
#     print(stack_close)
#
#     for i in range(length):
#         close_tag = stack_close.pop()
#         if close_tag == "(":
#             if right_close is True:
#                 # )) (( 일때
#                 left_close = True
#             left_close_count += 1
#         elif close_tag == ")":
#             right_close = True
#             right_close_count += 1
#
#     print(left_close,right_close,left_close_count, right_close_count)
#     if left_close_count != right_close_count or left_close is not True:
#         return False
#
#     return True


#강의 풀이
# 0123
# (())
# 0.괄호가 열렸다
# 1.괄호가 열렸다
# 2.1번째 인덱스의 괄호가 닫혔다
# 3.0번째 인덱스의 괄호가 닫혔다
#
# 01234
# ((())
# 0.괄호가 열렸다
# 1.괄호가 열렸다
# 2.괄호가 열렸다
# 3.2번째 인덱스의 괄호가 닫혔다
# 4.1번째 인덱스의 괄호가 닫혔다
#
# -> 닫는 괄호가 나오면, 바로 직전에 열렸었던 괄호가 닫힌다
# ->열린 괄호가 나오면 순서대로 쌓아서 저장해야한다
#-> 닫힌 괄호가 나오면 열린괄호를 하나 없앴다는 뜻에서 저장한걸 하나 뺀다
# -> 순서대로 데이터를 쌓아놓고, 가장 마지막에 생긴 데이터가 먼저 빠져나가는 형태의 자료구조
def is_correct_parenthesis(string):
    stack = []
    for i in range(len(string)):
        if string[i] == "(":
            stack.append("(")
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True

print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")()("))
