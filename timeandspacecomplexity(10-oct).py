#o(1)-constant time complexity
'''n=int(input("enter a number:"))
print(n+100)'''
#space complexity =o(1)

#O(n)-linear time complexity
#linear space complexity is o(1)
'''n=int(input("enter a number:"))
for i in range(1,n+1):
    print(i, end=' ')'''

#O(n)-linear time complexity
#linear space complexity is o(1)
'''n=int(input("enter a number:"))
arr=[]
for i in range(n):
    num=int(input("enter a value:"))
    arr.append(num)
print("list",arr)'''    
#in this code the time and space complexity is O(5)

#O(n^2) quadratic Time Complexity or pascal's triangle
'''n=int(input("enter n:"))
num=1
for i in range(n):
    for j in range(i):
        print(num, end=' ')
        num+=1
    print()'''

#
'''n=int(input("enter n:"))
num=1
for i in range(n):
    for j in range(n):
        print(num, end=' ')
        num+=1
    print()'''

#logarthmic Time Complexity
'''n=int(input("enter a value:"))
while n>1:
    print(n)
    n//=2
print(1)'''    

#logarthmic TC O(n(logn))
'''n=int(input("enter a value:"))
for i in range(n):
    j=n
    while j>1:
        j//=2
print("Done")'''        
        
#
def count(n):
    if n==0:
        return 1
    return count(n-1)+ count(n-1)
n=imt(input("enter a number:"))
print("result:", count(n))




