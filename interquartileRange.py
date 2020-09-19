#https://www.hackerrank.com/challenges/s10-interquartile-range/problem

num = int(input())
my_lst=map(int,input().split())
my_freq=map(int,input().split())
my_lst=list(my_lst)
my_freq=list(my_freq)

my_list =[]
for i in range(num):
    x= my_freq[i]
    while x> 0:
        my_list.append(my_lst[i])
        x -= 1

my_list.sort()

num=len(my_list)

def med_lst(n,lst):
    med_list=0
    if n % 2 == 0:
        med_list= (lst[int(n/2-1)]+lst[int(n/2)])/2
    else:
        med_list= lst[int((n-1)/2)]
    return float(med_list)


if num % 2 == 0:
    print(round(med_lst(int(num / 2), my_list[int(num / 2 ):]) - med_lst(int(num/2),my_list[:int(num/2)]),1))
else:
    print(round(med_lst(int((num-1)/2), my_list[int((num -1)/2 )+1:]) - med_lst(int((num-1)/2),my_list[:int((num-1)/2)]),1))