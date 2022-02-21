def multiple_of_10(number):
    """
    Multiple of 10 positive numbers starting 
    to count from the user number
    """
    if (number <= 0):
        print("The input number is less or equat to 0")
        return
    
    multiple = number

    for num in range(1,11):
        multiple *= num

    print(multiple)

# test function
multiple_of_10(1)
multiple_of_10(0)
multiple_of_10(-4)
multiple_of_10(2)