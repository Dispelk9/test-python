import copy
import math
import pylint

# Create List 
spam =['app','bana','tofu','cat']


def Ret(list_example):
    n = len(list_example)
    print(n)
    start_num = 0
    while True:
        print(list_example[start_num])
        if start_num < n:
            start_num += 1
        if start_num == n:
            ls = ' '.join(map(str,list_example))   # convert list to string
            print(ls)
            break
        
       

Ret(spam)    