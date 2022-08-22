#Marcxime Prosper Student ID: 009463957
from UI import *
from truck import *
import datetime


print("Hello, welcome to the project \n Here are your options: \n 1) Press 1 to get the status of the "
      "deliveries at a given time\n 2) Press 2 to search the deliveries within a range of times \n 3) Press 3 to show the "
      "total mileage \n 4) Press 4 to show individual packages information and statuses \n")

userInputMain = int(input("Please Enter 1, 2, 3, or 4: "))

if userInputMain == 1:
    print("\nPlease input the hour in 24 hour time \n")
    showAllPackagesWithGivenDeadlineTime()
elif userInputMain == 2:
    print("\nPlease input the hours in 24 hour time \n")
    startEnd()
elif userInputMain == 3:
    total = (truck1.mileage + truck2.mileage + truck3.mileage)
    print("\nThe total milage is: ", total)
elif userInputMain == 4:
    print("\nPlease input the hour in 24 hour time \n")
    showIndividualPackages()
else:
    print("\n Please run again and choose an option")

print("\nPlease run again to choose another option")







