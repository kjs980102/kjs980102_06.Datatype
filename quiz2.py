#다음 이중 리스트의 평균값을 아래 출력 결과와 같이 각각 구하여라.
my_list=[[100,200],[400,800],[1000,1400]]

# for nums in my_list:
#     a=(nums[0]+nums[1])/2
#     print(a)

for a in my_list:
    num=0
    for b in a:
        num=num+b
    last=(num/2)
    print(last)