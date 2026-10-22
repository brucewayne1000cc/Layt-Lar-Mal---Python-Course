import string
import random
import os

keyboard = (
    string.ascii_letters + string.digits + string.punctuation + ' '
)

password = 'laytlarmalpythoncourse'

seed = 0

for p in password:
    seed = seed * 8 + ord(p)

random.seed(seed)

keys = {
    key: str(random.randint(1000, 9999))
    for key in keyboard
}

digits = {str(value): key for key, value in keys.items()}

encrypted = None

message = None

def send(message):

    encryption = ''

    for m in message:
        encryption += keys[m] + ' '

    print('\nEncryption:', encryption)

    return encryption

def tryagain(encryption):
    read(encryption)

def read(encryption):

    decryption = ''

    digitsets = encryption.split()

    try:
        for d in digitsets:
            decryption += digits[d]

    except:
        os.system('cls' if os.name == 'nt' else 'clear')

        print('Message you entered:', message)

        print('\nEncryption:', encrypted)

        print('\nDecryption failed! Please try again.')

        tryagain(input('\nEnter your encryption: '))

        return None
        

    print('\nDecryption:', decryption)

    return decryption

os.system('cls' if os.name == 'nt' else 'clear')

message = input('Enter your message: ')

encrypted = send(message)

encryption = input('\nEnter your encryption: ')

read(encryption)