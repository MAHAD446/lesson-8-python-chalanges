print("enter anumber(numeretor):")
numn = int(input())
print("enter a number (denominator):")
numd = int(input())

if numn%numd==0:
    print("\n" +str(numn)+ " is divided by " +str(numd))
else:
    print("\n" +str(numn)+ " is not divided by " +str(numd))    