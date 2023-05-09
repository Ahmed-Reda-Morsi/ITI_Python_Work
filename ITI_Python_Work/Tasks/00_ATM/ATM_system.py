import datetime
#__________________________| ATM Data |______________________________
# define ATM valid accounts to use it.
Accounts={
    #'UserName': {'balance': amount , 'BIN': usr password}
    'Ahmed'  :{'Balance': 1500 , 'PIN': 4210 } ,
    'Ali'    :{'Balance': 6000 , 'PIN': 1234 },
    'Hassan' :{'Balance': 15000 , 'PIN': 9632 }
}

#define Set to hold all pins for valid accounts.
Accounts_Pins={1234,4210,9632}

# Tanscations information
Transactions_Info=[]


#___________________________| ATM Operations |_________________________________
""" User login operation function """
def ATM_Login():
    #check entered username
    UserName=input("Enter Your UserName: ")
    if UserName not in Accounts:
        print("UserName not found.")
        return False
    
    #check entered pin
    Pin=int(input("Enter your Pin: "))
    if Accounts[UserName]['PIN'] != Pin:
        print("Incorrect PIN.")
        return False
    # if Pin not in Accounts_Pins:
    #     print("Invalid PIN..")
    #     return False
    
    # if login is valid return username
    return UserName

""" User withdraw opertion function """
def ATM_Withdraw(UserName):
    amount= int(input("Enter amount to withdraw: "))
    if amount> Accounts[UserName]['Balance']:
        print("Sorry, Your balance is not enough!!")
        return False
    else:
        #update the balance
        Accounts[UserName]['Balance']-=amount
        Transaction_date_Time=datetime.datetime.now()
        #save this transation using tuple 
        Transactions_Info.append((UserName,'withdrawal',Transaction_date_Time,amount))
        print(f"Withdrawal successful. New balance is {Accounts[UserName]['Balance']}.")
        return True


""" User deposit opertion function """
def ATM_deposit(UserName):
    # take deposit amount from user.
    amount= int(input("Enter amount to withdraw: "))
    #update user balance
    Accounts[UserName]['Balance'] += amount
    Transaction_date_Time=datetime.datetime.now()
    #save this transation using tuple 
    Transactions_Info.append((UserName,'deposit  ',Transaction_date_Time,amount))
    print(f"Deposit successful. New balance is {Accounts[UserName]['Balance'] }.")
    return True



def ATM_UserViewBalance(UserName):
    print(f"Your balance is {Accounts[UserName]['Balance'] }.")
    return True

def ATM_ViewTransactions(UserName):
    for transaction in Transactions_Info:
        #show username  transaction type     transaction date_time
        if transaction[0]==UserName:
            print(f"User:{ transaction[0]} ,Transaction Type: {transaction[1]} ,Time: {transaction[2]} ,Amount:{transaction[3]}  ")


def ATM_System():
    UserName=True
    while True:
        UserName=ATM_Login()
        while UserName not in Accounts:
            print("Not Valid UserName please try again\n")
            UserName=ATM_Login()
        
        # User choose operation.
        print("\n________| Welcome to ATM System (._.) |________ \n please choose the operation you want.")
        print("\n__|(wd) -> Withdraw")
        print("\n__|(dp) -> Deposit")
        print("\n__|(vb) -> View balance")
        print("\n__|(vt) -> View transactions")
        print("\n__|(e)  -> Exit")
        choice=0
        while choice != 'e':
            choice =input("Enter your choosed operation: ")
            if choice == 'wd':
                ATM_Withdraw(UserName)
            elif choice == 'dp':
                ATM_deposit(UserName)
            elif choice == 'vb':
                ATM_UserViewBalance(UserName)
            elif choice == 'vt':
                ATM_ViewTransactions(UserName)
            elif choice == 'e':
                break
            else:
                print("Invalid choice. Try again.")
    


# Run ATM System.
ATM_System()