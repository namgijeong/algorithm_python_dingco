#for else 문
#for 문이 끝났을때 아무 일도 일어나지 않았다면 아래 있는 구문을 호출
#for문에서 만약 어떤 조건에 의해서 for문이 멈추게 된다면 이 else밑에 있는 코드는 실행이 되지 않음
for x in [1,2,3,4]:
    print(x)
    if x == 4:
        break

else:
    print("완료되었습니다.")



#소누는 자기 자신과 1 이외에는 아무것도 나눌 수 없다
input = 20

#내 풀이
# def find_prime_list_under_number(number):
#     #해당 수보다 작은 수들을 모조리 소수인지 검사
#     prime_list = []
#     for num in range(2, number):
#         #해당 수가 소수인가
#         is_prime = True
#         for i in range(1, num):
#             if i != 1 and num % i == 0:
#                 is_prime = False
#
#         if is_prime == True:
#             prime_list.append(num)
#
#     return prime_list

#강의 풀이
# def find_prime_list_under_number(number):
#     #2~20까지 찾아서
#     prime_list = []
#     for n in range(2, number + 1):
#         #이것들이 소수인가? 소수라면 prime_list에 넣어라
#         for i in range(2, n):
#             if n % i == 0:
#                 break
#         else:
#             prime_list.append(n)
#
#     return prime_list

#강의 풀이2
# def find_prime_list_under_number(number):
#     #2~20까지 찾아서
#     prime_list = []
#     for n in range(2, number + 1):
#         #n = 19
#         #i = 2~18까지 숫자들을 뽑아서
#         #19/2 , 19/3 , 19/6 ... => 이때 2,3으로 나누어떨어지지 않는다면 6으로도 나누어 떨어지지 않는다
#         #모든 수가 비교하는것이 아니라 소수들과만 비교하면 된다 => n보다 작은 모든 소수에 대해서 => 앞전에 사용했던 리스트를 활용
#
#         for i in prime_list:
#             if n % i == 0:
#                 break
#         else:
#             prime_list.append(n)
#
#     return prime_list


#강의 풀이3
def find_prime_list_under_number(number):
    #2~20까지 찾아서
    prime_list = []
    for n in range(2, number + 1):
        #n = 19
        #i = 2~18까지 숫자들을 뽑아서

        #N의 제곱근보다 크지 않은 어떤 소수로도 나누어 떨어지지 않는다.
        #i * i <= n
        #19/2 , 19/3만 비교하면 된다

        for i in prime_list:
            if i * i <=n and n % i == 0:
                break
        else:
            prime_list.append(n)

    return prime_list

result = find_prime_list_under_number(input)
print(result)