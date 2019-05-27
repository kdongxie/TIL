lunch = {
    '양즈강':'02-557-4211',
    "김밥까페":'02-553-3101',
    "순남시레기":'02-588-0887'
}
# 1. f-string
with open('lunch.csv','w',encoding='utf-8') as f:
    for item in lunch.items(): # [('양자강','02-557-4211'),(...),(...)]의 형태로 바뀐다.
        f.write(f'{item[0]},{item[1]}\n')

# 2.join()
with open('lunch2.csv','w',encoding='utf-8') as f:
    for item in lunch.items(): # [('양자강','02-557-4211'),(...),(...)]의 형태로 바뀐다.
        f.write(','.join(item)+'\n')

# 3.csv
import csv
with open('lunch3.csv','w',encoding='utf-8', newline="") as f:
    csv_writer=csv.writer(f)
    for item in lunch.items():
        csv_writer.writerow(item) # writerow 는 \n 이 기본적으로 포함되어 있다.따라서 newline을 설정한다.
