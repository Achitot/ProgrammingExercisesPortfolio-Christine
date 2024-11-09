name = input('Enter your name: ')
hometown = input('Enter your hometown:')

while True:
    age = input("Enter your age: ")
    if age.isdigit():
        age = int(age)
        break
    else:
        print("Please enter a number for your age.")

info = {
    "name": name,
    "hometown": hometown,
    "age": age
}

print(f"Name: {info['name']}")
print(f"Hometown: {info['hometown']}")
print(f"Age: {info['age']}")