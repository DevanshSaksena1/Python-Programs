no=int(input("Enter a number to find sum of all digits : "))
result=0
y=len(str(no))
while(y>0):
    x=no%10
    result=result+x
    no=no/10
print("your sum is "+result)
