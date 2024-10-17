#calcul dobanda

principal = 0 
rate = 0
time = 0

while principal <=0:
    principal = float(input("Enter the initial principal balance: "))
    if principal <=0:
        print("Can't be <=0")
        principal = float(input("Enter the initial principal balance: "))

while rate <=0:
    rate = float(input("Enter the rate: "))
    if rate <=0:
        print("Can't be <=0")
        rate = float(input("Enter the rate: "))

while time <=0:
    time = float(input("Enter the time in years: "))
    if time <=0:
        print("Can't be <=0")
        principal = float(input("Enter the time in years: "))

total = principal * pow((1+rate/100),time)

print(f"Balance after {int(time)} years/s is: {total: .2f} ")