import math
List_sum=[]
a = [1, 2, 3]
b = (4, 5, 6)

def sum(tuple,list):
    c = zip(tuple,list)
    for (x,y) in c:
        sum = [x+y]
        List_sum.append(sum)
    return print(List_sum)

sum(a,b)
