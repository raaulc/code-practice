def check_array_sorted(arr,index) -> bool:
    if index == 0:
        return True
    
    if arr[index] <= arr[index-1]:
        return False
    
    if arr[index] >= arr[index-1]:
        return check_array_sorted(arr,index-1)
    

arr = [10,20,30,40,50]
index = len(arr)-1
print(check_array_sorted(arr,index))