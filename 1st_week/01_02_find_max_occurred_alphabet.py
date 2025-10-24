def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for i in string :
        if i.isalpha() :
            alphabet_occurrence_array[ord(i)-ord('a')] += 1

    return alphabet_occurrence_array


print("정답 = [1, 0, 2, 2, 2, 0, 2, 1, 3, 0, 0, 2, 2, 3, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0] \n현재 풀이 값 =",
      find_alphabet_occurrence_array("hello my name is dingcodingco"))
print("정답 = [1, 0, 0, 0, 2, 0, 1, 1, 1, 0, 0, 2, 1, 0, 2, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0] \n현재 풀이 값 =",
      find_alphabet_occurrence_array("we love algorithm"))
print("정답 = [0, 3, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 3, 2, 0, 0, 0, 1, 0] \n현재 풀이 값 =",
      find_alphabet_occurrence_array("best of best youtube"))


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = find_alphabet_occurrence_array(string)
    max = alphabet_occurrence_array[0]
    maxIndex = 0
    for i in range(len(alphabet_occurrence_array)):
        if max < alphabet_occurrence_array[i]:
            max = alphabet_occurrence_array[i]
            maxIndex = i


    return chr(maxIndex+97)


result = find_max_occurred_alphabet


print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))


#2. [0*26] 각 알파벳의 빈도수를 저장한 배열을 만든다
#그리고 문자열을 돌면서 해당 문자가 알파벳이라면, 알파벳을 인덱스화 시켜서 알파벳의 빈도수를 업데이트 한다.
#a->0번째 인덱스 값을 올리고, z가 나왔다면 가장 마지막인 25번째 인덱스의 값을 추가해라

#문자인지 확인하는 방법
#파이썬의 내장 함수 str.isalpha() 를 이용

# 내장 함수 ord() 이용해서 아스키 값 받기
# print(ord('a'))               # 97
# print(ord('a') - ord('a'))    # 97-97 -> 0
# print(ord('b') - ord('a'))    # 98-97 -> 1

#아스키값을 문자로
#chr(97)