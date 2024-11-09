quiz = {
    "Germany": "Berlin",
    "Spain": "Madrid",
    "Italy": "Rome",
    "Austria": "Vienna",
    "France": "Paris",
    "United Kingdom": "London",
    "Greece": "Athens",
    "Netherlands": "Amsterdam",
    "Sweden": "Stockholm",
    "Switzerland": "Bern"
 }

points = 0 

for country, capital in quiz.items():
    answer = input(f"What is the capital for {country}? ").capitalize()
    if answer == capital.capitalize():
        print('Your answer is correct!')
        points += 1
    else:
        print(f'Your answer is wrong, the correct answer is {capital}.')

print(f'You got {points} out of {len(quiz)} correct.')

