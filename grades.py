print("Enter your marks in your five main subjects!:  ")
markOne= int(input("Mark one:  "))
markTwo= int(input("Mark two:  "))
markThree = int(input("Mark three:  "))
markFour = int(input("Mark four:  "))
markFive = int(input("Mark five:  "))

tot = markOne + markTwo + markThree + markFour + markFive
avg =tot/5

if avg >= 90 and avg <= 100:
    print ("A Grade")
elif avg >= 80 and avg < 90:
    print ("B Grade")
elif avg >= 65 and avg < 80:
    print ("C Grade")
elif avg >= 40 and avg < 65:
    print ("D Grade")
else:
    print ("F Grade")
