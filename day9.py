def calculate_tax():
    print("=" * 50)
    print("       TAX ANALYTICS ENGINE - BACKEND TERMINAL  ")
    print("=" * 50)

    try:
        # User input handling with standard float precision
        annual_income = float(input("[INPUT] Enter your Total Annual Income (₹): "))
    except ValueError:
        print("[ERROR] Invalid monetary value entered. Please restart.")
        return

    # Initializing standard state variables
    calculated_tax = 0.0
    tax_slab = ""

    # Professional Range-Bound Conditional Architecture
    if annual_income <= 300000:
        calculated_tax = 0.0
        tax_slab = "0% (Tax-Free Zone)"

    elif 300000 < annual_income <= 600000:
        calculated_tax = (annual_income - 300000) * 0.05
        tax_slab = "5% Bracket"

    elif 600000 < annual_income <= 900000:
        # 15000 is the constant accumulated tax from previous slab
        calculated_tax = 15000 + (annual_income - 600000) * 0.10
        tax_slab = "10% Bracket"

    else:
        # 45000 is the standard total accumulated tax from previous 2 slabs
        calculated_tax = 45000 + (annual_income - 900000) * 0.20
        tax_slab = "20% Premium Bracket"

    # Net payroll deduction math
    net_take_home = annual_income - calculated_tax

    # System Ledger Output Report
    print("\n" + "-" * 20 + " FINANCIAL SYSTEM LEDGER " + "-" * 20)
    print(f"Gross Annual Income   : ₹ {annual_income:,.2f}")
    print(f"Active Tax Bracket    : {tax_slab}")
    print(f"Total Evaluated Tax   : ₹ {calculated_tax:,.2f}")
    print(f"Net Post-Tax Salary   : ₹ {net_take_home:,.2f}")
    print("-" * 65)

# Driver code execution
calculate_tax()