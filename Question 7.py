import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

for i in range(len(random_numbers)):
    if random_numbers[i] > 50:
        random_numbers[i] = random.randint(20, 30)
    else:
        random_numbers[i] = "XX"

print(random_numbers)

# Lines 1-6 What we are doing here is for the numbers between 1 and 100 picked randomly
#Lines 7-12 What we are doing here that if the number is greater than 50 and number has to be between 20 and 30, otherwise we will put an XX
