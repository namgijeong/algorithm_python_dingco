array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


#내 풀이
def merge(array1, array2):
    array_c = []
    a_index = 0
    a_length = len(array1)
    b_index = 0
    b_length = len(array2)
    c_index = 0
    c_length = len(array1) + len(array2)
    while c_index <= c_length-1:
        if a_index == a_length:
            for i in range(b_index, b_length):
                array_c.append(array2[i])
                c_index += 1
            #array_c.append(array2[b_index:])
        elif b_index == b_length:
            for i in range(a_index, a_length):
                array_c.append(array1[i])
                c_index += 1
            #array_c.append(array1[a_index:])
        else:
            if array1[a_index] >= array2[b_index]:
                array_c.append(array2[b_index])
                b_index += 1
                c_index += 1
            else:
                array_c.append(array1[a_index])
                a_index += 1
                c_index += 1

        print(array_c)
    return array_c


#강의 풀이
def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0

    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else :
            result.append(array2[array2_index])
            array2_index += 1

    while array1_index < len(array1):
        result.append(array1[array1_index])
        array1_index += 1

    while array2_index < len(array2):
        result.append(array2[array2_index])
        array2_index += 1

    return result

print("정답 =",merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))