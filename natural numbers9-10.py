#today we deal in 1-D/2-D data structures
#natural numbers
'''n=int(input("enter n:"))
for i in range(1,n+1):
    if i%2==1:
        print(i, end=' ')'''
#square pattern with numbers
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        print(i, end=' ')
    print()'''    

'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        print(j, end=' ')
    print()'''    

'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()'''    
#hallow square pattern
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print('*', end=" ")
        else:
            print(" ",end=" ")
    print()'''
#hallow square pattern with diagonals
#n-1-i or i+j=n-1
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or i+j==n-1:
            print('*', end=" ")
        else:
            print(" ",end=" ")
    print()'''        
        
#hour zone
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1  or i==j or i+j==n-1:
            print('*', end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1  or i==j or i+j==n-1:
            print('*', end=" ")
        else:
            print(" ",end=" ")
    print()'''
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==n//2 or j==n//2:
            print('*', end=" ")
        else:
            print(" ",end=" ")
    print()'''
#hollow pattern with * in 2-D data with * in middle 
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1 or i==n//2 or j==n//2:
            print('*', end=" ")
        else:
            print(" ",end=" ")
    print()'''
#2-D priting pattern by removing the sides
n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if  i==j or i+j==n-1:
            print('*', end=" ")
        else:
            print(" ",end=" ")
    print()

