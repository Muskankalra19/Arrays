from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :

	# Your code here
    max_current= max_global=arr[0]
    
    for i in range (1, n):
        max_current= max(arr[i], max_current+ arr[i])
        
        if max_current > max_global:
            max_global = max_current
    if (max_global>=0):
        return max_global;
    else:
        return 0;
