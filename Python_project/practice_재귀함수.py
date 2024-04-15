# def countdown(n):
#     if n > 0:
#         print(n)
#         countdown(n-1)

# countdown(4)

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return factorial(n-1) * n

# print(factorial(3))
# print(factorial(5))
# print(factorial(6))

# def reverse(my_list):
#     if len(my_list) <= 1:
#         return my_list
#     #어자피 위에 return 에서 이 함수가 종료되기 때문에 else를 굳이 안쓰고 해도됨
#     return my_list[-1:] + reverse(my_list[:-1])

# print(reverse([5, 2, 1, 7, 4]))


# 피보나치수열-재귀함수
# my_list = [1,1]
# def fib(n):
#     if n <= len(my_list):
#         return my_list[n-1]
#     new_value = fib(n-1) + fib(n-2)
#     my_list.append(new_value)
#     return new_value
# # 테스트 코드
# for i in range(1, 16):
#     print(fib(i))



#자릿수의 합
# def sum_digits(n):
#     if n<10:
#         return n
#     else:
#         return sum_digits(n//10) + (n%10)
    
    
# # 테스트 코드
# print(sum_digits(22541))
# print(sum_digits(92130))
# print(sum_digits(12634))
# print(sum_digits(704))
# print(sum_digits(3755))

#펠린드롬
def is_palindrome(my_str):
    if len(my_str) <= 1:
        return True
    else:
        if my_str[0] != my_str[-1]:
            return False
        return is_palindrome(my_str[1:-1])


# 테스트 코드
print(is_palindrome('기러기'))
print(is_palindrome('토마토'))
print(is_palindrome('바나나'))
print(is_palindrome('racecar'))
print(is_palindrome('radar'))
print(is_palindrome('stars'))
print(is_palindrome('123321'))

#숫자의 거듭제곱
def power(x, n):
    if n==0:
        return 1
    elif n==1:
        return x
    temp = power(x, n // 2)
    if n % 2 == 0:
        #짝수일때
        return temp * temp
    else:
        #홀수일때
        return x * temp * temp
            


# 테스트 코드
print(power(2, 3))
print(power(5, 0))
print(power(17, 5))
print(power(3, 17))
print(power(4, 18))