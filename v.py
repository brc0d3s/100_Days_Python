print("Enter the narration (press Enter twice to end):")

narration = ""

while True:
    line = input()
    if line == "":
        break
    narration += line + "\n"

with open("hinton.txt", "w") as file:
    file.write(narration)
