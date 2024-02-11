password=input("Write your password: ")


length = len(password)
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
# special_characters = {'@', '#', '$', '%'}
has_special = any(char in {'@', '#', '$', '%'} for char in password)


if len(password) <8:
    print("Weak: Password must be at least 8 characters long.")
elif not (has_upper and has_lower):
    print("Weak: Password must be Upper and lower Case")
elif not has_digit:
    print("Weak: Password must be digit")
elif not has_special:
    print("Weak: Password must a special Char.")
else:
    print("Correct!")