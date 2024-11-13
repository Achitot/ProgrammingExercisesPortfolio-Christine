password = 12345
while True:
    enter = int(input("enter password: "))

    if enter == password:
        print("Correct password!")
        break
    else:
        print("Incorrect password! Try again.")