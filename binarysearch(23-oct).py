#types of searchs:
'''1.Linear
2.Binary
3.Jump Search'''

#Binary Search
'''arr=list(map(int,input("Enter the values:").split()))
arr.sort()
val=int(input("enter a element to search:"))
low=0
high=len(arr)-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==val:
        print("element found at mid",mid)
        break
    elif arr[mid]<val:
        low=mid+1
    else:
        high=mid-1
else:
    print("element not found")'''

#find the square root of a number using binar search pattern
'''val=int(input("enter the element:"))
low=0
high=val
while low<=high:
    mid=(low+high)//2
    if mid*mid==val:
        print("square root:",mid)
        break
    elif mid*mid<val:
        low=mid+1
    else:
        high=mid-1
else:
    print("integer square root",high)'''
