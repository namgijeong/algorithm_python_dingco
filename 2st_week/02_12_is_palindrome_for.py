input = "abcba"

#내 풀이
# def is_palindrome(string):
#     length = len(string)
#     print(string, length)
#     if length == 1:
#         return True
#
#     start_index = 0
#     last_index = length - 1
#     if (string[start_index] == string[last_index]):
#         return is_palindrome(string[start_index + 1:last_index])
#     else:
#         return False

# 강의 풀이
def is_palindrome(string):
    if string[0] != string[-1]:
        return False

    if len(string) <= 1:
        return True

    return is_palindrome(string[1:-1])


print(is_palindrome(input))