import math
from typing import List


def print_loop(n):
    # Base case to stop recursion
    if n <= 0:
        return
    print_loop(n - 1)
    print(n)

# Example usage

def print_array(arr, idx=0):
    # Base case: stop when index reaches length of array
    if idx >= len(arr):
        return
    print_array(arr, idx + 1)
    print(arr[idx])


def search_array(arr, target, idx=0):
    # Base case: if index reaches length of array, target not found
    if idx >= len(arr):
        return -1
    if arr[idx] == target:
        return idx
    return search_array(arr, target, idx + 1)

def find_min(arr,idx=0,min=math.inf):
    if len(arr) == 0:
        return -1 
    
    if idx >= len(arr):
        return min 

    min = min if min < arr[idx] else arr[idx]

    return find_min(arr,idx + 1,min)

def find_max(arr,idx=0,max=-math.inf):
    if len(arr) == 0:
        return -1 
    
    if idx >= len(arr):
        return max 

    max = max if max > arr[idx] else arr[idx]

    return find_max(arr,idx + 1,max)

def print_digits(num):
    if(num == 0):
        return 
    
    digit = num%10
    num = num//10
    # recursive code 
    print_digits(num)
    print(digit)





# Example usage
my_list = [10, 20, 30,1987, 40, 50]
# print(search_array(my_list,40)) 
# print(find_max(my_list))

print_digits(48382)