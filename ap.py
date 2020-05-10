def ap(a,d,l):

    while(a<=l):
        print(a)
        a=a+d

a=int(input("Enter first term of ap : "))
d=int(input("Enter difference between two terms of ap : "))
n=int(input("Enter number of terms in ap : "))

l=a+((n-1)*d)

ap(a,d,l)
