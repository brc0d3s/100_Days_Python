readFile = open("file.txt","r")

if readFile:
    content = readFile.read()
    print("File contents: \n",content)

readFile.close()