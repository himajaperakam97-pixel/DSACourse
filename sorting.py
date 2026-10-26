#sorting
'''1.bubble sort
2.selection sort
3.insertion sort'''
#bubblesort
'''arr=list(map(int, input("enter elements ").split()))
n=len(arr)
for i in range(n):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1]=arr[j+1], arr[j]
print(*arr)'''

#selection sort
'''arr=list(map(int, input("enter elements").split()))
n=len(arr)
for i in range(n):
    minindex=i
    for j in range(i+1, n):
        if arr[j]<arr[minindex]:
            minindex=j
    arr[i], arr[minindex]=arr[minindex], arr[i]
print(*arr)'''

#insertion sort
arr=list(map(int, input("enter elements ").split()))
n=len(arr)
for i in range(n):
    x= arr[i]
    j= i-1
    while j>=0 and arr[j]>x:
        arr[j+1]= arr[j]
        j-=1
    arr[j+1]=x
print(*arr)    
        



