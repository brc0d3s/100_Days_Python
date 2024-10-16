#open the file.txt in read mode. causes error if no such file exists.    
fileptr = open("file.txt","r");     
    
#stores all the data of the file into the variable content    
content = fileptr.readlines()     
  
#prints the content of the file    
print(content)     
    
#closes the opened file    
fileptr.close()   