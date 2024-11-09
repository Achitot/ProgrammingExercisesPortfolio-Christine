password = "12345"
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    user_input = input("Enter password: ")
    if user_input == password:
        print("Access granted!")
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Incorrect password. You have {remaining} attempt(s) left.")
        else:
            print("Incorrect password. The authorities have been alerted.")
            break
