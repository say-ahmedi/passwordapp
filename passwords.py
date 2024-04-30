import secrets
import random
import string


lowletters= [l for l in string.ascii_lowercase]
upletters=[l for l in string.ascii_uppercase]

letters=lowletters+upletters
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']

nr_letters=random.randint(8,10)
nr_numbers=random.randint(2,4)
nr_symbols=random.randint(2,4)

#creating list to save the password details

def generatePassword():
    #using list comprehensions to modify our code
    password_letters=[random.choice(letters) for _ in range(nr_letters)]
    password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
    password=password_letters+password_numbers+password_symbols
    random.shuffle(password)
    return ''.join(password)
