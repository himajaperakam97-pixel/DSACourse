#array - data types under one roof
#traverse a array and add 100 to each element
'''arr=list(map(int, input("Enter elements").split()))
for val in arr:
    print(val+100, end=' ')'''

#summate the values in an array
'''arr=list(map(int, input("Enter elements:").split()))
total=0
for val in arr:
    total+=val
print("Sum: ",total)'''


#maximum value in an array
'''arr=list(map(int, input("Enter elements:").split()))
maximum=arr[0]
for val in arr:
    if val>maximum:
        maximum=val
print("largest value:",maximum)'''        


#minimum value in an array

'''arr=list(map(int, input("Enter elements:").split()))
minimum=arr[0]
for val in arr:
    if val<minimum:
        minimum=val
print("smallest value:",minimum)'''

#reverse an array
'''arr=list(map(int, input("Enter elements:").split()))
for val in range(len(arr)-1, -1, -1):
    print(arr[val], end=' ')'''


#remove the duplicates in an array
'''arr=list(map(int, input("Enter elements:").split()))
result=[]
for val in arr:
    if val not in result:
        result.append(val)
print(*result)'''

#count of even and odd numbers in an array
'''arr=list(map(int, input("Enter elements:").split()))
even=0
odd=0
for val in arr:
    if val%2==0:
        even+=1
    else:
        odd+=1
print("Even : ",even)
print("odd : ",odd)'''

#rotate an array clockwise direction
'''arr=list(map(int, input("Enter elements:").split()))
k=int(input("Enter rotations: "))
k%=len(arr)
arr=arr[k:]+arr[:k]
print(*arr)'''

#rotate an array anticlockwise direction
'''arr=list(map(int, input("Enter elements:").split()))
k=int(input("Enter rotations: "))
k%=len(arr)
arr=arr[-k:]+arr[:-k]
print(*arr)'''

























