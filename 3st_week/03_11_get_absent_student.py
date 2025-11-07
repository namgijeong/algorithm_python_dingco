all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

# class LinkedTuple:
#     def __init__(self):
#         self.items = []
#
#     def add(self, key, value):
#         self.items.append((key, value))
#
#     def get(self, key):
#         for k, v in self.items:
#             if k == key:
#                 return v
#
#
# class LinkedDict:
#     def __init__(self, length):
#         self.items = []
#         for i in range(length):
#             self.items.append(LinkedTuple())
#
#     def put(self, key, value):
#         index = hash(key) % len(self.items)
#         self.items[index].add(key, value)
#
#     def get(self, key):
#         index = hash(key) % len(self.items)
#         return self.items[index].get(key)


#내 풀이
# def get_absent_student(all_array, present_array):
#     # 해시테이블로 만들기
#     length = len(all_array)
#     linked_dict = LinkedDict(length)
#     for member in present_array:
#         linked_dict.put(member, member)
#
#     for all_member in all_array:
#         #print(linked_dict.get(all_member))
#         if linked_dict.get(all_member) is None:
#             return all_member
#
#     return "모두 출석"


#강의 풀이 1
# 1.2중 반복문
# for student in all_students:
#     is_present = False
#     for present_student in present_students:
#         if student == present_student:
#             is_present = True
#     if not is_present:
#         return student
    
#2. 정렬
# 정렬 이후에 하나하나 원소들을 보면서 존재하지 않는 학생을 찾으면 결석한 친구를 찾을 수 있음


#강의 풀이2
#3. dictionary, hash table
#all_students를 돌면서, hash table의 키값에 해당 학생들을 등록한다
#present_students를 돌면서 hash table의 키값의 값을 제거한다
#그리고 나서 남아있는 hash table의 키 값에 해당하는 학생이 결석한 학생이다
def get_absent_student(all_array, present_array):
    dict = {}
    for student in all_array:
        #존재하는가만 보기 위해서이므로 True가 아닌 다른 아무 값이나 넣어도 된다
        dict[student] = True

    for present_student in present_array:
        del dict[present_student]

    #이 문제에서는 결석한 사람이 무조건 한명이기 때문에
    for key in dict.keys():
        return key


print(get_absent_student(all_students, present_students))

print("정답 = 예지 / 현재 풀이 값 = ",get_absent_student(["류진","예지","채령","리아","유나"],["리아","류진","채령","유나"]))
print("정답 = RM / 현재 풀이 값 = ",get_absent_student(["정국","진","뷔","슈가","지민","RM"],["뷔","정국","지민","진","슈가"]))