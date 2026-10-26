#Approaches
#math,Naive,BruteForce,greedy,BackTracking

#math approach - Strong number
'''n=int(input("enter a number:"))
copy=n
total=0
while n!=0:
    d=n%10
    f=1
    i=1
    while i<=d:
        f*=i
        i+=1
    total+=f
    n//=10
if total==copy:
    print(copy,"is a strong number")
else:
    print(copy,"is not a strong number")'''


#1/2!+2/3!+3/4!+.....n
'''n=int(input("enter a number"))
total=0
f=1
for i in range(1,n+1):
    f*=i+1
    total+=i/f
print("Sum:", total)'''    

#naive approach - find the occurences of a number
'''arr=list(map(int, input("Enter elements:").split()))
value=int(input("Enter value:"))
count=0
for i in arr:
    if i==value:
        count+=1
print(value, "Occurences are:", count)'''        

#BruteForce approach - finding all possibilities
'''arr=list(map(int, input("enter elements:").split()))
target=int(input("enter value"))
count=0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]+arr[j]==target:
            print(arr[i], arr[j])'''

#14-10-26 continuity for yesterday session
#greedy approach
'''coins=list(map(int, input("enter coins:").split()))
amount=int(input("enter amount:"))
total_count=0
for coin in coins:
    count=amount//coin
    if count>0:
        print(coin, "rupees:",count)
        total_count+=count
        amount%=coin
print("total coins: ", total_count)'''

#BackTracking
'''n=int(input("enter n:"))
def backtrack(s):
    if len(s)==n:
        print(s)
        return
    backtrack(s+"0")
    backtrack(s+"1")
backtrack("")'''    

#tail recursion with backtracking
'''def num(n):
    if n==0:
        return
    num(n-1)
    print(n, end=' ')
n=int(input("enter n:"))
num(n)'''
#head recursion
'''def num(n):
    if n==0:
        return
    print(n, end=' ')
    num(n-1)
n=int(input("enter n:"))
num(n)'''

#nested recursion
def func(n):
    if n>10:
        return n
    return (func(func(n+2)))
n=int(input("enter n:"))
print(func(n))            



















