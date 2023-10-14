height= int(input("Enter your heigh in cm :\t"))
age=int(input("Enter your age : \t"))

if height > 120 :
    print("Can ride !")
    if age > 18:
        print("Pay $12 ")
    else:
        print("Pay $7 ")

else:
    print("Can't ride !")