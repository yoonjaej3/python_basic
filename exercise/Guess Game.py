import random

guess_number=random.randint(1, 100)

correct_time=0
while 1:
    print("숫자를 입력하세요")
    num = int(input())
    if num ==guess_number:
        print(correct_time,"번만에 정답입니다.")
        break;
    elif num>guess_number:
        print("숫자가 너무 큽니다.")
        correct_time+=1
    else:
        print("숫자가 너무 작습니다.")
        correct_time+=1

