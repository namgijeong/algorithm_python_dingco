input = "abcba"


def is_palindrome(string):
    final_index = len(string)-1
    if final_index == 0:
        return True
    if string[0] == string[final_index]:
        return is_palindrome(string[1:final_index])
    else:
        return False

print(is_palindrome(input))