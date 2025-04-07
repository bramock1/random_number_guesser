import random
def guess_random_number(tries, start, stop):
    random_number = random.choice(range(start,stop+1))
    while tries != 0:
        print(f"{tries} tries left.")
        guess = int(input("Guess the number: "))
        if guess > random_number:
            print("Guess lower")
        elif guess < random_number:
            print("Guess higher")
        else:
            print("You guessed the correct number!")
            break
        tries -= 1

# Test task 1
# guess_random_number(5, 0, 10)

def guess_random_num_linear(tries, start, stop):
    random_number = random.choice(range(start, stop+1))
    while tries != 0:
        for i in range(start, stop):
            print(f"The program is guessing...{i}")
            if i == random_number:
                print("The program has guessed the right number")
                return i
            elif i != random_number:
                tries -= 1
                print(f"Number of tries left: {tries}")
                if tries == 0:
                    print("The program has failed to guess the correct answer")
                    break


# Test Task 2
# guess_random_num_linear(5, 0, 10)

def guess_random_number_binary(tries, start, stop):
    random_number = random.choice(range(start, stop+1))
    num_list = range(start, stop+1)
    lower_bound = 0
    upper_bound = len(num_list) - 1
    while lower_bound <= upper_bound and tries > 0:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = num_list[pivot]
        if pivot_value == random_number:
            print(f"Found it: {pivot_value}")
            return pivot
        elif pivot_value > random_number:
            print("Guessing lower")
            upper_bound = pivot - 1
        else:
            print("Guessing higher!")
            lower_bound = pivot + 1
            tries -= 1
            print(f"{tries} tries left")
    print("Your program failed to find the number")
# Test task 3
# guess_random_number_binary(5, 0, 100)