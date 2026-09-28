correct_pin ="1234"
attempts = 3 
print("WELCOME TO SECURE ATM SYSTEM")

while attempts>0:
    user_pin=input(f"\n Enter your 4-digit PIN (Attempts left:{attempts}):")
    
    if user_pin==correct_pin:
        print("Login Successful! Access Granted.")
        break
    else:
        print("Incorrect PIN! Please try again.")
        attempts-=1
if attempts==0:
    print("\n [SECURITY ALERT] 3 Wrong attempts. Your ATM Card is BLOCKED for 24 Hours!")