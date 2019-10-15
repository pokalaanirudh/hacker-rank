#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    x=n-d
    l=[]
    for i in range(n):
        if i< d:
            l.insert(x,a[i])
            x+=1
        else:
            l.insert(i-d,a[i])    

    for i in range(n):
        print(int(l[i]),end=" ")
