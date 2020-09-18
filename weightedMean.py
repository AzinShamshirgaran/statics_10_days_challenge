num = int(input())
my_list=map(int,input().split())
my_list=list(my_list)
my_weights=map(int,input().split())
my_weights=list(my_weights)
sum_m=0
for i in range(num):

    sum_m += my_list[i]*my_weights[i]

print(round(sum_m/sum(my_weights),1))