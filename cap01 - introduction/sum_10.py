def sum_of_10(number):
    """
    Sum of 10 positive numbers starting 
    to count from the user number
    """
    if (number < 0): 
        print("The input number is less then 0")
        return
    
    sum_next = number

    for num in range(11):
        sum_next += num

    print(sum_next)

# test the function
sum_of_10(10)
sum_of_10(-5)
sum_of_10(3)