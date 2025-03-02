#Fernando Guzman
#02/28/25

#Function multiplies list of numbers

def multiply_list(numbers):
    value = 1 # Initializing value within the function
    for x in numbers:
       value = value * x
    return value

numbers = [ 5 , 2 , 7 , -1]

print(multiply_list(numbers))
