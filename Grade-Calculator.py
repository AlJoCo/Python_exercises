print("Thank you for using the Grade Calculator")
mathsmark = int(input("Please enter your mark for maths: "))
physicsmark = int(input("Please enter your mark for physics: "))
chemistrymark = int(input("Please enter your mark for chemistry: "))

totalpercentage = float(mathsmark + physicsmark + chemistrymark) / 3
print(f"Your total percentage score is: {totalpercentage}%")
if totalpercentage > 70:
    print("You achieved an A")
elif totalpercentage >= 60:
    print("You achieved an B")
elif totalpercentage >= 50:
    print("You achieved an C")
elif totalpercentage >= 40:
    print("You achieved an D")
else: print("You failed")