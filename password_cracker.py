import string
import itertools
import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument('--pass_length', type=int, default=0, help='password length.')
parser.add_argument('--uppercase', action='store_true', default=False, help='add uppercase letters to password.')
parser.add_argument('--numbers', action='store_true', default=False, help='add numbers to password.')
parser.add_argument('--symbols', action='store_true', default=False, help='add symbols to password.')

args = parser.parse_args()

lowercase_alphabet = 'abcdefghijklmnopqrstuvwxyz'
uppercase_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '~!@@#$%^&*()-_~[]{};:|,./<>?'


password_space = lowercase_alphabet

common_passwords = ['password', '123456', '12345678', 'qwerty',
'abc123', 'monkey', '1234567', 'iloveyou', '111111', '123123',
'qwerty123', '1q2w3e4r', 'baseball', 'dragon', 'qwertyuiop']

keylogger_text = 'TOBIdfdscmwciwrr3vbeo3ro3b3rbtobithegreat300@gmail.compassword123dfrerv0w'


def generate_password(length=3):
    if args.uppercase:
        add_uppercase()
    if args.numbers:
        add_numbers()
    if args.symbols:
         add_symbols()

    password = ''
    for i in range(args.pass_length):
        password += random.choice(password_space)

    return password


def add_uppercase():
    global password_space
    password_space += uppercase_alphabet

def add_numbers():
    global password_space
    password_space += numbers

def add_symbols():
    global password_space
    password_space += symbols

def password_guesser_brute_force(password, guess = ''):
    global guess_counter

    if len(guess) == 0:
        guess_counter = 0
    if len(guess) == len(password):
        guess_counter += 1
        if guess == password:
            print('Got {} after {} tries'.format(guess, guess_counter))
            return True
        return False
    else:
        for character in password_space:
            if password_guesser_brute_force(password, guess + character):
                return True
        return False

def create_random_password_and_guess():
    password = generate_password(args.pass_length)
    password_guesser_brute_force(password)

create_random_password_and_guess()
