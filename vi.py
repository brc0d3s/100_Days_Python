with open("hinton.txt", "r") as file:
    content = file.read()

sentences = content.split(".")  

for i, sentence in enumerate(sentences, start=1):
    sentence = sentence.strip()  
    if sentence:  
        print(f"{i}. {sentence}.")
