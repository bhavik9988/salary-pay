
def computepay(h,r):
    return 24.14
x=input("enter no. of hours:")
hrs=int(x)
y=input("enter no. of rate:")
rate=float(y)
if hrs<40:
    pay=hrs*rate
elif hrs>=60:
    pay=(50*rate)+(hrs-50)*rate*1.5

print("Pay",pay)

