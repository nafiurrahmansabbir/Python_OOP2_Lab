char=input("Enter a single string: ")

check= any(char in {'a','e','i','0','u','A','E','I','O',} for char in char)

if(len(char)==1)and(char.isalpha()):
    if check:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalit Input!")
