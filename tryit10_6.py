prompt1 = "Enter first number : "
prompt2 = "Enter second number : "

try:
    answer1 = input(prompt1)
    answer2 = input(prompt2)
    result1 = int(answer1)
    result2 = int(answer2)
    print(f"The sum of those 2 numbers is : {result1 + result2}")
except ValueError:
    print("Sorry! You haven't put number as input.")
    pass

