

print("ATM")
print("1. Check balance")

print("2. Deposit cash")

print("3. Withdraw cash")

print("4. Exit ")
choice= [1,2,3,4]
choice= int(input("Enter an input "))


depositCash=0
balance= depositCash+0
withdrawCash=0

if choice==1:
        print(f"Your balance is: {balance}$")
elif choice==2:
        depositCash= int(input("Enter deposit amount: "))
        print(f"Your account balance is: {balance + depositCash}$")
elif choice==3:
        withdrawCash= int(input("Enter withdrawal amount: "))
        print(f"Your remaining account balance is: {balance-withdrawCash}")

