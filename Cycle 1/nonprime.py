a=int(input("enter the lower bound:"))
b=int(input("enter the upper bound:"))
nonprime=[]
print("prime numbers are:")
for num in range(a,b+1):
    if num < 2:
        nonprime.append(num)
    else:
        for i in range(2,int(num**0.5)+1):
            if num % i ==0:
                nonprime.append(num)
                break
print(nonprime)









