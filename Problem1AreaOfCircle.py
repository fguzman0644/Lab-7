#Fernando Guzman
#02/28/25

#Function that calculates the radius of a circle

import math

def area_of_circle(pi,r):
    return round(pi*(r**2),2)

pi = float(math.pi)
r = float(input("Enter radius of circle: "))
print("The area of your circle is ", area_of_circle(pi,r))
    
