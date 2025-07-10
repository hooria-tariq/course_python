sentence = input("Enter a sentence: ").lower()  

for x in sentence:
    if x in "aeiou":  
        vowel_count += 1

print(f"Total vowels found: {vowel_count}")