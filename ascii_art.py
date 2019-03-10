from pyfiglet import figlet_format
from termcolor import colored


text = input("What message do you want to print? ")

# Available text colors: [red, green, yellow, blue, magenta, cyan, white]
color = input("What color? ").lower()

try:
    modify_text = colored(figlet_format(text, font='standard'), color=color)
except KeyError:
    modify_text = colored(figlet_format(text, font='standard'), color='magenta')
    print(f"Sorry we don't have color {color}.")

print(modify_text)









