# mhmd amin

#the string of vowels
vowels = 'aeuio'
TheSentence = input("enter your string: ")
#make a dictionary with each vowel a key and value 0

count = {}.fromkeys(vowels,0)
#count the vowels
for char in TheSentence:
    if char in count:
        count[char] += 1

print(count)
