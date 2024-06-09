n=int(input("Enter how many values you want to read: "))
array=[]
sum=0
for i in range(n):
    val=int(input(f"Enter the value of a[{i}]:"))
    array.append(val)
    sum+=val
print("The sum of array elements=",sum)
