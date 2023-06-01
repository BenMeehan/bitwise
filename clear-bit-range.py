i=int(input())
j=int(input())
n=int(input())
a=~0
a=a<<i+1
b=(1<<j)-1

k=a|b


print(n&k)