import random


def get_random_number(lower_int, upper_int):
    return random.randint(lower_int, upper_int)

low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))

random_number = get_random_number(low, high)

print(random_number)
