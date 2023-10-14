LIFE = 90
age =int(input("Enter your current age : \t"))
years_left=LIFE - age

months_left=years_left * 12
weeks_left=years_left * 52
days_left =years_left * 365


print(f"You have {days_left}days {weeks_left}weeks and  {months_left}months left")