num=int(input("enter the three digit number"))
a=num%10
num=num//10
b=num%10
num=num//10
c=num%10
print("reverse of the number id",a*100+b*10+c)
