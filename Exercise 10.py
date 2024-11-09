def checking(number):
    if number % 2 == 0:
        print(f"The {number} is EVEN.")
    else:
        print(f"The {number} is ODD")
def main():
    number_input = int(input("Enter any number: "))
    result = checking(number_input)
    print(result)

if __name__ == "__main__":
    main()
