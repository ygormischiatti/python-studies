user = "John Doe"
ip = "1.2.3.4"
attempts = 5
blocked = False

if attempts > 10:
    risk = "HIGH"
elif attempts >= 6:
    risk = "MEDIUM"
else:
    risk = "LOW"

print(f"Risk: {risk}")

if risk == "HIGH" and not blocked:
    print("Necessary action: Block user")