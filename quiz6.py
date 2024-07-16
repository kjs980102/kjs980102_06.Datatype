#1부터 100까지의 수를 2의 배수, 3의 배수, 5의 배수로 분류하려고 한다.

numbers_1=[]
numbers_2=[]
numbers_3=[]

for a in range(1,101):
    if a%2==0:
        numbers_1.append(a)
    if a%3==0:
        numbers_2.append(a)
    if a%5==0:
        numbers_3.append(a)
print(numbers_1)
print(numbers_2)
print(numbers_3)