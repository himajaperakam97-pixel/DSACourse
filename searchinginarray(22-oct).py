#Searching in Arrays 1D/2D
#1.search an element and return its index value in a 1-D array
'''arr=list(map(int, input("enter values: ").split()))
search=int(input("Enter element to be searched: "))
found= False
for i in range(len(arr)):
    if arr[i]==search:
        print("element found at:", i)
        found= True
        break
    if not found:
        print("element out of range")'''

#searching of array 2-D
'''n=int(input("Enter the size:"))
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))
search=int(input("Enter element to be searched:"))
found= False
for i in range(n):
    for j in range(n):
        if arr[i][j]==search:
            print("element found at row:", i, "col:", j)
            found= True
            break
if not found:
    print("element out of range")'''
#sum of an array
'''n=int(input("Enter the size:"))
s=0
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        s+=arr[i][j]
print("total:",s)'''

#adding an individual element in an array
'''n=int(input("enter the size:"))
s=0
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))
    s=0
    for j in range(n):
        s+=arr[i][j]
    print("Row :", i+1, "sum :" ,s)
print()
for j in range(n):
    s=0
    for j in range(n):
        s+=arr[i][j]
        print("col :", j+1, "sum:" ,s)'''

n=int(input("enter the size:"))
arr=[]
di=0
ad=0
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if i==j:
            di +=arr[i][j]
        if i+j==n-1:
            ad +=arr[i][j]
print("Diagonal sum: ",di)
print("Anti-Diagonal sum: ",ad)


























            



