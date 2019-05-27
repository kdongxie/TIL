import random
number = range(1,45)
lotto = random.sample(number,6)
# print(lotto)
print(f'이번주 행운의 로또 번호는 {sorted(lotto)}입니다.')

