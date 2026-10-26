#Divide and conquer
'''1.Merge sort
2.Quick sort'''
#merge sort
def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=mergesort(arr[:mid])
    right=mergesort(arr[mid:])
    result=[]
    while left and right:
        if left[0]<right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result+left+right
arr=list(map(int, input("enter elements: ").split()))
print(mergesort(arr))


