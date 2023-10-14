cat_mark=int(input("enter the cat mark out of 30 \n:"))
main_exam=int(input("enter the main exam mark out of 70 \n:"))
final_exam=cat_mark+main_exam

if 100>= final_exam >=70:
    grade="A"
elif 69>= final_exam >=60:
    grade="B"
elif 59>= final_exam >=50:
    grade="C"
elif 49>= final_exam >=40:
    grade="D"
elif 39>= final_exam >=00:
    grade="F"
else :
    grade="invalid choice"

    
print(f"your grade is :{grade}" )  
