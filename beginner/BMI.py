weight=float(input("Enter your weight in KG : \n"))
height=float(input("Enter your height in M : \n"))

BMI=int(weight/height**2)

if BMI >= 35 :
    print("Clinically Obese ")
elif 30 <= BMI < 35 :
    print("Obese ")
elif 25 <= BMI < 30 :
    print("Over weight ")
elif 18.5 <= BMI < 25 :
    print("Normal Weight ")
else:
    print("Underweight ")