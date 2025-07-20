sentence = input("Enter a sentence: ").lower()  
vowel_count=0

for x in sentence:
    if x in "aeiou":  
      vowel_count += 1

print(f"Total vowels found: {vowel_count}")