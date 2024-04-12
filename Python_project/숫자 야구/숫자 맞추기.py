import random
num = random.randint(1,20)
def corret_num(num):
    for i in range(1,5):
        answer = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(5-i)))
        if answer == num:
            print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(i))
            return
        elif answer < num:
            print("Up")
        elif answer > num:
            print("Down")
    print("아쉽습니다. 정답은 {}입니다.".format(num))   

corret_num(num)
