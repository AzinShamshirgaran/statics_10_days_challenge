from math import sqrt
num = int(input())
my_lst=map(int,input().split())
my_lst=list(my_lst)
mean_my_list= sum(my_lst)/num
my_q=[]
for i in range(num):
    my_q.append((my_lst[i]-mean_my_list)**2)
print(round(sqrt(sum(my_q)/num),1))