import random 
import string
def gen_pass(length):
    upper=string.ascii_uppercase
    lower=string.ascii_lowercase
    digits=string.digits
    special=string.punctuation
    all=upper+lower+digits

    x=input("Need Special Characters (Y or N)?").strip().lower()
    if x=='y':
        all+=special
    password= ''.join(random.choice(all) for _ in range(length))
    return password
length=int(input("Enter length:"))
print("generated pass is:",gen_pass(length))