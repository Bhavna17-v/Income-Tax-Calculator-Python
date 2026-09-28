# Day 11: Automated Banking Account Ledger System
# Developer: Bhavna (B.Sc. Computer Science)

print("=" * 50)
print("       WELCOME TO APEX DIGITAL BANKING LEDGER   ")
print("=" * 50)

# 1. Base State Setup (Initial Balance)
account_balance = 5000.0  # Default savings balance

# 2. Infinite Loop to keep the software running
while True:
    print("\n--- MAIN MENU ---")
    print("1. Check Account Balance")
    print("2. Deposit Money (Jama Karein)")
    print("3. Withdraw Money (Nikaalein)")
    print("4. Exit Securely")
    
    
    choice = input("\nSelect an option (1-4): ")
    
    # 3. Decision Control Architecture
    if choice == "1":
        print(f"\n[BALANCE REPORT] Your current available balance is: ₹ {account_balance:,.2f}")
        
    elif choice == "2":
        deposit_amount = float(input("Enter amount to deposit (₹): "))
        
        # Safety Check: Zero ya negative money entry block karna
        if deposit_amount > 0:
            account_balance += deposit_amount
            print(f"Success! ₹ {deposit_amount:,.2f} credited to your account.")
            print(f"Updated Balance: ₹ {account_balance:,.2f}")
        else:
            print("[ERROR] Invalid amount! Deposit must be greater than zero.")
            
    elif choice == "3":
        withdraw_amount = float(input("Enter amount to withdraw (₹): "))
        
        # Safety Check: Insufficient balance system lock
        if withdraw_amount > account_balance:
            print(f"[TRANSACTION DECLINED] Insufficient Balance! Available: ₹ {account_balance:,.2f}")
        elif withdraw_amount <= 0:
            print("[ERROR] Invalid amount! Withdrawal must be greater than zero.")
        else:
            account_balance -= withdraw_amount
            print(f"Success! ₹ {withdraw_amount:,.2f} debited from your account.")
            print(f"Updated Balance: ₹ {account_balance:,.2f}")
            
    elif choice == "4":
        print("\nThank you for banking with us! Session closed securely. 🔐\n")
        break  
        
    else:
        print("[INVALID CHOICE] Please select a valid option between 1 and 4.")
