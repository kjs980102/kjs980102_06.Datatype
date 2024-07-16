#네 자리수의 덧셈 함수, 곱셈 함수 코드를 각각 작성하시오.
def num_code(num1,num2,num3,num4):
    result=num1+num2+num3+num4
    print('합계:',result)
    return result

def num_code2(num1,num2,num3,num4):
    result=num1*num2*num3*num4
    print('곱:',result)
    return result

num_code2(1,5,2,10)
code_add=num_code2
print(code_add)