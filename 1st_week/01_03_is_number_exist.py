#빅오 -> 최악의 경우 
#빅오메가 -> 최선의 경우
def is_number_exist(number, array):
    for i in array:
        if number == i:
            return True  #시간 복잡도는 N만큼 걸린다

    return False;



result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))
print("정답 = Flase 현재 풀이 값 =", result(7, [6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))

