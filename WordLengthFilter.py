sentence = input("Enter a sentence: ")
x=sentence.split()
longWords=[]
for word in x:
    if len(word)>4:
        longWords.append(word)

print("Words longer than 4 letters:", longWords)