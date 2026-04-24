Account_bal=100000
card='c'
pwd=1234
while True:
    n=input("Insert the card=")
    if n==card:
        print("welcome, Tripura")
        b=int(input("enter the password:"))
        if b==pwd:
            option=int(input("options: 1. Bal enquiry 2. Withdraw"))
            if option==2:
                x=int(input("withdraw amount:"))
                print(f"Account balance is {Account_bal-x}")
            else:
                print(f"Account balance is {Account_bal}")
        else:
            print("Incorrect Password")
    else:
        print("Invalid card")




    
