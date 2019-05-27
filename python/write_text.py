# Write File
# 1. open
# f = open('mulicam.txt', 'w') # w= Write / r = Read / a = Append
#
# for i in range(10):
#     f.write(f'Hello, Multi_campus{i} \r\n') # \r 은 한출 띄기 \n 은 다음줄로 작성하기
# f.close()

# 2. with open() / close()가 필요 없다.
# with open('mulcam2.txt', 'w') as f:
    # f.wirte('Hello Mulcam: \n')

# 2-1. wirtelines / 내용이 꼭 list의 형태로 들어가야 한다.
# with open('mulcam3.txt','w') as f:
#     f.writelines(['1\n','2\n','3\n'])

# write : Context Manager
# \ 로 시작하는 문자 -> 이스케이프 시퀀스(문자)
# \n : 가행 문자
# \t : tab 문자
# \\n : 역슬레쉬 문자를 그래도 입력할 때
# \' : 따옴표 문자
# \" : 쌍따옴표 문자

# 예제
# print("Let's go")
# print('Let\'s go')

