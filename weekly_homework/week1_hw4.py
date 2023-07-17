a=float(input("the 1st term of AP(a):"))
d=float(input("common difference(d):"))
n=int(input("n:"))
sum=0
for i in range(n):
    sum=sum+1/(a+i*d)
print("sum=",sum)