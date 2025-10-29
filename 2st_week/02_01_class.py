class Person:
    #pass  # 여기서 pass 는 안에 아무런 내용이 없다는 의미입니다!

    def __init__(self, name_param):
        self.name = name_param
        print("hihi i am created", self, self.name)

    def talk(self):
        print("안녕하세요 저는", self.name, "입니다.")


person_1 = Person("유재석")
person_2 = Person("박명수")
person_1.talk()
person_2.talk()
