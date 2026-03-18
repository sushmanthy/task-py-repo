#Count char in string
str=input("Enter a string:")
count=0
for char in str:
    count=count+1
print("number of char in this str:", count)


#Count Vowels
str=input("Enter a string:")
vowels= "aieous"
vowel_count=0
for char in str:
    if char in vowels:
        vowel_count=vowel_count+1
print("vowels:", vowel_count)

#Consonants

str=input("Enter a string:")
vowels= "aieous"
vowel_count=0
for char in str:
    if char not in vowels:
        vowel_count=vowel_count+1
print("consonants:", vowel_count)

#Reverse

str=input("Enter a string:")
reverse=""
for char in str:
    reverse=char+reverse
print("reverse the string:", reverse)

name="sushmanth"
print(name[ : : -1])

#Palindrome
str=input("Enter a string:")
if str==str[: :-1]:
    print("string is palindrome")
else:
    print("string is not palindrome")