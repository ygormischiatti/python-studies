attempts_list = [1, 3, 6, 8, 10, 11, 14, 20]
high_count = 0

for attempts in attempts_list:
    if attempts > 10:
        risk = "HIGH"
        high_count += 1
    elif attempts >= 6:
        risk = "MEDIUM"
    else:
        risk = "LOW"
    
    print(f"Attempts: {attempts} -> Risk: {risk}")

print(f"Total HIGH risks detected: {high_count}")