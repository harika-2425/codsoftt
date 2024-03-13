import string
import random
def generate(length):
    characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(characters) for _ in range(length))
    return password
length=int(input('Enter the lenth of the password: '))
password=generate(length)
print(f"password: {password}")