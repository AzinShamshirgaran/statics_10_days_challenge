#https://www.hackerrank.com/challenges/s10-quartiles/problem

from math import floor
num = int(input())
my_list=map(int,input().split())
my_list=list(my_list)
my_list.sort()

def med_lst(n,lst):
    med_list=0
    if n % 2 == 0:
        med_list= (lst[int(n/2-1)]+lst[int(n/2)])/2
    else:
        med_list= lst[int((n-1)/2)]
    return floor(med_list)


if num % 2 == 0:
    print(med_lst(int(num/2),my_list[:int(num/2)]))
    print(med_lst(num, my_list))
    print(med_lst(int(num / 2), my_list[int(num / 2 ):]))
else:

    print(med_lst(int((num-1)/2),my_list[:int((num-1)/2)]))
    print(med_lst(num, my_list))
    print(med_lst(int((num-1)/2), my_list[int((num -1)/2 )+1:]))