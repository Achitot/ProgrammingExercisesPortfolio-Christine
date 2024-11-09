calendar = {
    1: "31",
    2: "28",
    3: "31",
    4: "30",
    5: "31",
    6: "30",
    7: "30",
    8: "31",
    9: "30",
    10: "31",
    11:"30",
    12:"31"
}
year = int(input("Enter the year: "))
 #leap year = year/4= 0 
 #except for years that are exactly divisible by 100 
 #year/400"

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    calendar[2] = "29"

while True:
    answer = int(input(f"Enter the month number (1-12): "))
    if 1 <= answer <= 12:
        print(f"The month number {answer} has {calendar[answer]} days.")
        break  
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")