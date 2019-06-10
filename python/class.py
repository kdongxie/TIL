class person:
    name = '사람의 고유한 속성',
    age = '출생이후 부터 삶을 마감할 때 까지의 시간',

    def greeting(self):
        print(f'{self.name} 이 인사합니다. 안녕하세요?')

    def eating(self):
        print(f'{self.name} 은 밥을 먹고 있습니다.')

    def aging(self):
        print(f'{self.name}은 현재 {self.age}세 이고, 현재 나이를 먹어가는 중 입니다.')


Bob = person()
print(Bob.name)
print(Bob.age)
Bob.name = 'Bob'
Bob.age = 31
print(Bob.name)
print(Bob.age)
Bob.greeting()
Bob.eating()
Bob.aging()
