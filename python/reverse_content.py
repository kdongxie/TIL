'''
multicam3.txt 의 파일의 내용[1,2,3]을 역순[3,2,1]으로 바꾸러 저장하시오
'''
with open('mulcam3.txt','w') as f:
    f.writelines(['1\n','2\n','3\n'])
#
with open('mulcam3.txt', 'r') as f:
    line = f.readlines()
    line.reverse()

with open('mulcam4.txt', 'w') as f:
    f.writelines(line)

