while 1:
    print("구구단 몇 단을 계산할까요(1~9)?")
    dan = int(input())

    if dan == 0 or dan == 10:
        print("구구단 게임을 종료합니다.")
        break;

    print("구구단",dan,"단을 계산합니다.")

    for idx in range(1,10):
        print(dan,"X",idx)

