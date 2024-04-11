from random import randint


#번호뽑기
def generate_numbers(n):
    numbers = []
    for i in range(n):
        num = randint(1,45)
        numbers.append(num)
    return numbers


#당첨 번호뽑기
def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]


#겹치는 번호 개수
def count_matching_numbers(numbers, winning_numbers):

    count = 0
    for i in range(len(winning_numbers)):
        if winning_numbers[i-1] in numbers:
            count += 1
    return count


#당첨확인
def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])
    if count == 6:
        return 1000000000
    elif count == 5:
        if bonus_count == 1:
            return 50000000
        else:
            return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0
        
        

# 테스트 코드
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))
