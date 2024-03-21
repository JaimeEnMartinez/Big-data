# Exercise 1: Is a Number Prime?
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    num = int(input("Enter an integer: "))
    if is_prime(num):
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")

# Exercise 2: Next Prime

def next_prime(n):
    n += 1
    while True:
        if is_prime(n):
            return n
        n += 1

if __name__ == "__main__":
    num = int(input("Enter an integer: "))
    print("The next prime number after", num, "is:", next_prime(num))

# Exercise 3: Median of Three Values
def median_of_three(num1, num2, num3):
    nums = [num1, num2, num3]
    nums.sort()
    return nums[1]

if __name__ == "__main__":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    print("The median is:", median_of_three(num1, num2, num3))

# Exercise 4: Random Password
import random

def generate_random_password():
    length = random.randint(7, 10)
    password = ""
    for _ in range(length):
        password += chr(random.randint(33, 126))
    return password

if __name__ == "__main__":
    print("Randomly generated password:", generate_random_password())

# Exercise 5: Compute the Hypotenuse
def compute_hypotenuse(side1, side2):
    hypotenuse = (side1**2 + side2**2)**0.5
    return hypotenuse

if __name__ == "__main__":
    side1 = float(input("Enter the length of the first shorter side: "))
    side2 = float(input("Enter the length of the second shorter side: "))
    print("The length of the hypotenuse is:", compute_hypotenuse(side1, side2))
