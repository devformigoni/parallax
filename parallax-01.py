### Program developed by Prof. MSc. Paulo O. Formigoni, PhD ###
### profpauloformigoni@gmail.com ###


### The program calculates the distance between the observer and a distant object using parallax.
### The user inputs the values of the two legs (cateto A and cateto B) of a simple parallax device and
### the value of the reference leg (cateto C), which is perpendicular to the line between the observer and
### the distant object.

#
#             o   <- object _____________________________
#                                                      /
#                                                     /
#                                                    /
#                                                   /
#        ___   <-cateto A                          /
#       /                                         /  <- distance from observer to object
#      /  <- cateto B                            /
#     /                                         /
#    /                                         /
#   /---------/  <- cateto C                 _/_

import math

def calc_distance(A, B, C):
    d = 100 * C * math.sqrt(A**2 + B**2) / B
    # d = distance of the object (in meters),
    # C = reference leg (in meters),
    # A = cateto A (in centimeters),
    # B = cateto B (in centimeters).
    return d

A = float(input("Enter the value of leg A (in centimeter): "))
B = float(input("Enter the value of leg B (in centimeter): "))
C = float(input("Enter the value of leg C (in meters): "))

distance = calc_distance(A, B, C)

print("The object's distance is: ", distance, "meters")
