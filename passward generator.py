import secrets
import string

letters=string.ascii_letters
   # print(letters)
digits=string.digits
    #print(digits)
special_chars=string.punctuation
    #print(special_chars)
alphabet=letters+digits+special_chars
pas_length=6
pas=""
for i in range(pas_length):
        pas +=''.join(secrets.choice(alphabet))
        print(pas)