class Dict:
    def __init__(self):
        self.items = [None] * 8

    # 충돌이 발생한다
    # a   b  c  d  e  ... z
    # [0,  1,  ..8]  26개인데 8개밖에 자리가 없으니까
    # 1.chaining 기법 : 충돌이 발생했을때 그 값들을 링크드 리스트로 관리한다
    # self.items[1] = [7] -> [6]
    # 이렇게하면 충돌 인덱스가 1일때 7을 꺼내야할지 6을 꺼내야할지 알수없다
    # self.item[1] = ["333", 7] -> ["77", 6]
    # hash("333") % len(self.items) -> index -> 1
    # self.items[1] -> ["333",7] -> ["77",6]
    # ["333", 7]에 있네! 그러면 value는 7이야
    def put(self, key, value):
        key = hash(key) % 8
        self.items[key] = value

    def get(self, key):
        key = hash(key) % 8
        return self.items[key]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))  # 3이 반환되어야 합니다!
