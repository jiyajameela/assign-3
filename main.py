###############################1
correct_username = "python"
correct_password = "rules"

attempts = 0

# we should be sure if its correct login or allow only 5 attempts
while attempts < 5:
    # Ask user for username and password
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if username and password are correct
    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        print("Incorrect username or password. Please try again.")
        attempts = attempts + 1

# If 5 attempts are reached and login is still incorrect
if attempts == 5:
    print("Access denied")

##############################2
import random

# Ask the user how many dice to roll

number_dice = int(input("Enter the number of dice to roll: "))

total_sum = 0

#calculate the sum by rolling the dice
for _ in range(number_dice):
    # Roll the die
    dice_roll = random.randint(1, 6)
    print(f"Roll {_ + 1}: {dice_roll}")
    total_sum += dice_roll
    # Add the roll to the total sum

# Print the total sum of the numbers rolled
print("Sum of the all the numbers:", total_sum )

########################3
numbers = []

# Ask the user to enter numbers until an empty string is entered
while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    try:
        # Converting the user input to a float
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Sort the numbers in descending order
greatest_numbers = sorted(numbers, reverse=True)[:5]
# get the five greatest integer
# Print the five greatest numbers
print("The five greatest numbers:")
for num in greatest_numbers:
    print(num)

#########################4
# create an empty list to store city names
city_list = []

# a for loop to read city names from the user
for i in range(5):
    city_name = input("Enter the name of a city: ")
    city_list.append(city_name)

#use print and for to list out the cities you mentioned
print("Cities that you entered:")
for city in city_list:
    print(city)

##########################5

import random

def roll_dice():
    return random.randint(1, 6)

def main():
    while True:
        # Call the roll_dice function to get a random dice roll
        dice_result = roll_dice()

        # Print the result of each roll
        print("Dice roll result:", dice_result)

        # Break the loop if the result is 6
        if dice_result == 6:
            print("You rolled a 6!")
            break


# Call the main function to run the program
if __name__ == "__main__":
    main()

########################6
# Function to convert gallons to liters
def gallons_to_liters(gallons):
    return gallons * 3.78541  # 1 gallon is approximately 3.78541 liters

def main():
    while True:
        # Ask the user for the quantity of gasoline in gallons
        gallons = float(input("Enter the quantity of gasoline in  gallons (or put in a negative value to quit): "))

        # Check if the input is negative; if it is , make an exit
        if gallons < 0:
            print(" you are exiting the program . ")
            break

        # Convert gallons to liters using the function and print the result
        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons is equal to {liters:.2f} liters.")


# Call the main function to run the program
if __name__ == "__main__":
    main()



