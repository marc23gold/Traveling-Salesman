#Marcxime Prosper Student ID: 009463957
from UI import *
import datetime


print("Hello welcome to the project \n Here are your options: \n 1) Press 1 to get the list of "
      "deliveries \n 2) Press 2 to search the deliveries with a range of times \n 3) Press 3 to show the "
      "total milage \n 4) Press 4 to show individual packages \n")

userInputMain = int(input("Please Enter 1, 2, 3, or 4: "))

if userInputMain == 1:
    print("\nPlease input the hours in 24 hour time \n")
    showAllPackagesWithGivenDeadlineTime()
elif userInputMain == 2:
    startEnd()
elif userInputMain == 3:
    print("\nPlease input the hours in 24 hour time \n")
    print("\nThe total milage is: ", 128.9)
elif userInputMain == 4:
    print("\nPlease input the hours in 24 hour time \n")
    showIndividualPackages()
else:
    print("\n Please run again and choose an option")

print("\n Please run again to choose another option")







