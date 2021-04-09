import webbrowser
from datetime import datetime
timenow = datetime.now()

""" TIME  """
print(timenow)

""" USERS  """
admin = "BowBoy"

""" GREETING  """
WelcomeUser = f"Hello {admin}!    What would you like to do today, Sir?"
print(WelcomeUser)

""" Pressing Numbers  """
press_1 = "Press: 1 to go to BowBoyCoDeRepo on GitHub"
print(press_1)

press_2 = "Press: 2 to go to Google"
print(press_2)

print("Press any other number and it will open all the above!")

""" Taking input from the user as integer & printing enter number """
# this is a container=num for the input - data type = int
num = int(input("Enter a number:"))

# if num = number go to site - note: new=2 means open in a tab if availible
if num == 1:
    # open blog
    webbrowser.open('https://github.com/BowBoyGit/BowBoyCoDeRepo', new=2)
elif num == 2:
    # open google
    webbrowser.open('https://www.python.org', new=2)
else:
    # print to screen pronto and open 2 browsers
    print("you need to add more options! Pronto!!!")
    webbrowser.open('https://github.com/BowBoyGit/BowBoyCoDeRepo', new=2)
    webbrowser.open('https://www.python.org', new=2)
