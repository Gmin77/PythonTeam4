#<<<<<<< HEAD
def plus(a,b):
    return a+b

def divide(a,b):
    return a/b 
    
#>>>>>>> gyeongmin

def subtract_numbers():
    num1 = float(input("뺄셈 할 첫 번째 숫자를 입력하세요: "))
    num2 = float(input("뺄셈 할 두 번째 숫자를 입력하세요: "))

    result = num1 - num2
    print("뺄셈 결과: ", result)

subtract_numbers()
#>>>>>>> hanjun

num1 = int(input("첫번째 숫자 : "))
num2 = int(input("두번째 숫자 : "))

def multiply(x, y):
    return x * y

print(num1,"*",num2,"=", multiply(num1,num2))