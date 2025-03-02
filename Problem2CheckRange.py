#Fernando Guzman
#02/28/25

#Function checks whether a number is in a given range

def check_range(number):
    if 1 <= number <= 10:
        return("Number is within range.")
    else:
        return("Number is not within range.")

number = int(input("Please enter a number: "))
print(check_range(number))
