#write a program to add the digits of a given number
'''n=int(input("enter a number:"))
s=0
while n!=0:
    d=n%10
    s=s+d
    n//=10
print("sum:",s)'''

#reverse a given number
'''n=int(input("Enter a number:"))
rev=0
while n!=0:
    d=n%10
    rev=(rev*10)+d
    n//=10
print(rev)'''

#generate n even numbers
#method-1
'''n=int(input("enter n:"))
for i in range(n):
    if i%2==0:
        print(i,end=' ')
    i=i+1'''    
#method-2
n=int(input("enter n:"))
i=1
while i<=n:
    if i%2==0:
        print(i,end=' ')
    i+=1    
    
