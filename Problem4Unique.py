#Fernando Guzman
#02/28/25

#python function takes a list of numbers and returns new list with unique elements of the first list.

def unique_elements(numbers):
    unique_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

numbers = [1 , 3 , 3 , 3 , 6 , 2 , 3 , 5]
new_list = unique_elements(numbers)

print(new_list)
