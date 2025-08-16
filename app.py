users = []
def create_account():
    user = {}
    user['fullname'] = input("Enter your full name: ")
    user['phone_number'] = input("Enter your phone number: ")
    user['password'] = input("Create a password: ")
    user['NIN'] = input("Enter your NIN: ")
    while True:
        try:
            user['balance'] = float(input("Enter amount to deposit (minimum $50): "))
            if user['balance'] < 50:
                print("Minimum deposit is $50. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
    users.append(user)
    print("Account created successfully!")
    
def view_details():
    phone_number = input("Enter your phone number to view details: ")
    for user in users:
        if user['phone_number'] == phone_number:
            print("User Details:")
            print(f"Full Name: {user['fullname']}")
            print(f"Phone Number: {user['phone_number']}")
            print(f"Balance: ${user['balance']}")
            print(f"NIN: {user['NIN']}")
            return
    print("User not found.")

def transfer():
    phone_number = input("Enter your phone number to transfer funds: ")
    for user in users:
        if user['phone_number'] == phone_number:
            destination_phone = input("Enter destination phone number: ")
            amount = float(input("Enter amount to transfer: "))
            if amount > user['balance']:
                print("Insufficient funds.")
            else:
                for dest_user in users:
                    if dest_user['phone_number'] == destination_phone:
                        user['balance'] -= amount
                        dest_user['balance'] += amount
                        print(f"Transfer successful! New balance: ${user['balance']}")
                        return
                print("Destination user not found.")
            return
    print("User not found.")
def main():
    while True:
        print("Welcome to Microfinance Bank")
        print("1) Create Account")
        print("2) View My Details")
        print("3) Transfer Funds")
        print("4) Exit")
        choice = input("Please select an option: ")
        
        if choice == '1':
            create_account()
        elif choice == '2':
            view_details()
        elif choice == '3':
            transfer()
        elif choice == '4':
            print("Thank you for using Microfinance Bank. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()
