import math  # module for math functions
from turtle import *  # turtle package for graphics

def hearta(k):
    """
    Y-coord of heart shape
    """
    return 15 * math.sin(k)**3  # Parametric equation for y-coord

def heartb(k):
    """
    X-coord of heart shape
    """
    return 12*math.cos(k) - 5*math.cos(2*k) - 2*math.cos(3*k) - math.cos(4*k)  # Parametric equation for x-coord

# Set draw speed
# Set background
speed(1000)
bgcolor("black")

# Create Turtle Screen
screen = Screen()

# Sets the window to be always on top
screen.getcanvas().winfo_toplevel().attributes("-topmost", 1)


# Prompts Welcome Message 
print("\nWelcome to HeartMaker♡")
print("A program so thoughtful that it draws you a heart forever. Let's watch a heart get drawn!\n")

# Define colors list
color_options = ["red", "aquamarine", "white", "orchid", "gold", "blue"]

# Prints color options list
print("Color Options:")
for i, color in enumerate(color_options):
    print(f"{i+1}. {color}")

# Loop gets user choice
while True:
    try:
        # Prompts user to select choice (as int)
        color_choice = int(input("\nEnter number of color: "))
        # Evaluate user choice (int)
        if 1 <= color_choice <= len(color_options):
            chosen_color = color_options[color_choice - 1]
            break
        else:
            print("Uh-oh! Please select a valid option from the list.")
    except ValueError:
        print("Sorry. Please enter a number.")

# Iterates over range of values to get heart shape
for i in range(6000):
    goto(hearta(i) * 20, heartb(i) * 20)
    pencolor(chosen_color)
    goto(0, 0)

done()