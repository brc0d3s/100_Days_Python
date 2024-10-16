# Pyprogram to print even nums from 50 to 20 using for loop

sum = 0

for i in range(50,19,-1):
    if i % 2 == 0:
        print(i)
        sum += i
print(f"Sum is {sum}")
   
