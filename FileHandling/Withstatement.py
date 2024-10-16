with open("file.txt","w+") as f:
    f.write("Hello lucky \nHow are you doing")

    f.seek(0)

    cont = f.read()
    print(cont)

    f.close()