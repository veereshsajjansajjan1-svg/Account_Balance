import sys

if len(sys.argv) != 3:
    print("Usage: python bank_balance.py <initial_balance> <deposit_amount>")
    sys.exit(1)

initial_balance = float(sys.argv[1])
deposit_amount = float(sys.argv[2])

updated_balance = initial_balance + deposit_amount


print("\n--- Bank Account Balance ---")
print(f"Initial Balance: {initial_balance:.2f}")
print(f"Deposit Amount: {deposit_amount:.2f}")
print(f"Updated Balance: {updated_balance:.2f}")
