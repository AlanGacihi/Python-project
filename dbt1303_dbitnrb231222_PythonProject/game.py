import random

# Generate a random number between 0 and 10000000
secret_number = random.randint(0, 1000000)

def main():
    
    # Continuously prompt user to guess a number
    while(True):
        user_input = int(input("Guess a number: "))

        if user_input > secret_number:
            print("Your guess is greater than the secret number.")
        elif user_input < secret_number:
            print("Your guess is less than the secret number.")
        else:
            print("Your guess is correct!")
            break

        # Compare digits  
        compare_digits(user_input, secret_number)


def compare_digits(user_input, secret_number):
    """
    Compare digits in the input and secret number and determine
    how many digits have been guessed correctly in the correct 
    place and how many digits have been guessed correctly but in 
    the wrong place.
    """
    # Convert user input and secret number to string 
    user_input = str(user_input)
    secret_number = str(secret_number)
    
    # Initialize correctly placed and wrongly placed digits
    wrong_place = 0
    correct_place = 0
    checked = []
    
    # Determine number with less digits
    if len(user_input) > len(secret_number):
        shortest_length = len(secret_number)
    elif len(user_input) < len(secret_number):
        shortest_length = len(user_input)
    else:
        shortest_length =  len(secret_number)
    
    # Determine digits guessed correctly in right place
    for i in range(shortest_length):
        if secret_number[i] == user_input[i]:
            correct_place += 1
            checked.append(user_input[i])
    
    # Determine digits gussed correctly in wrong place
    for digit1 in user_input:
        for digit2 in secret_number:
            if digit1 == digit2 and digit1 not in checked:
                wrong_place += 1
                checked.append(digit1)
    
    print(f"{correct_place} digits have been guessed correctly in the right place")
    print(f"{wrong_place} digits have been guessed correctly in the wrong place")


if __name__ == "__main__":
    main()
