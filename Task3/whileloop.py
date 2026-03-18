#Print numbers using while
num=1
while num<=20:
     print(num)
     num=num+1

#factorial of a number
num=int(input("Enter a number"))
fact=1
i=1
while (i<=num):
    fact=fact*i
    i=i+1
print(fact)

#Diff code

num=int(input("Enter a number"))
fact=1
while (num>1):
    fact=fact*num
    num=num-1
print(fact)

#Count Digits

n=int(input("Enter a number:"))
count=0
while n!=0:
    n=n//10
    count=count+1
print(count)