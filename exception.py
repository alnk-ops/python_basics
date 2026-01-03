try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    print(a/b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
# valueError exception
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
finally:
    print("Execution completed.")

# to view the balance of a bank account
try:
    balance=5000
    withdraw_amount=int(input("Enter amount to withdraw: "))
    if withdraw_amount>balance:
        raise Exception("Insufficient funds in your account.")
    balance-=withdraw_amount
    print("Withdrawal successful. Remaining balance:", balance)
except Exception as e:
    print("Error:", e)