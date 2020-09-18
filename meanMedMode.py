#https://www.hackerrank.com/challenges/s10-basic-statistics/problem

import numpy as np
len_my_list = int(input())
my_list=np.array(input().split(),int)
my_list=list(my_list)
my_list.sort()
mean_my_list = sum(my_list)/len_my_list
#print("{:.1f}".format(mean_my_list))
print(round(mean_my_list,1))
if len_my_list %2 == 0:
    print(round((my_list[int(len_my_list/2)-1]+my_list[int(len_my_list/2)])/2,1))
else:
    print(round(my_list[int(len_my_list/2)+1]/2,1))

dic_my_list={}
for i in range(len_my_list):
    if my_list[i] in dic_my_list:
        dic_my_list[my_list[i]] += 1
    else:
        dic_my_list[my_list[i]] = 1
print( max(dic_my_list, key=dic_my_list.get))