#Generates a specified amount of text files with cryptographically sercure psuedorandom strings and numbers

#Imports and variable setup

import secrets
import os
from pathlib import Path
import shutil

verbose_message = ' characters.'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

#Creation functions


#Header, title, and credits

print(f"\n{bcolors.HEADER}\n=- ranDum File Generator -={bcolors.ENDC}")

#Options and setup
print(f"{bcolors.BOLD}\nFile Settings{bcolors.ENDC}")

print(f"{bcolors.OKGREEN}\nHow many files would you like to generate in total?{bcolors.ENDC}")
file_num_to_gen = input('>> ')

print(f"{bcolors.BOLD}\nText Settings{bcolors.ENDC}")

print(f"{bcolors.OKGREEN}\nHow many lines of numbers would you like to generate per txt file?{bcolors.ENDC}")
num_to_gen = input('>> ')

print(f"{bcolors.OKGREEN}\nHow many bytes should each line contain (1 byte = 2 digits){bcolors.ENDC}")
byte_length = input('>> ')
byte_length = int(byte_length)

print(f"{bcolors.BOLD}\nVerbose and Log Settings{bcolors.ENDC}")

print(f"{bcolors.OKGREEN}\nShow file creation status and log? y/n{bcolors.ENDC}")
creation_verbose = input('>> ')

if creation_verbose == ('y' or 'yes' or 'ye'):
     creation_verbose = True
     verbose_message = (' characters, with log.')
else:
     creation_verbose = False
     verbose_message = (' characters.')

print(f"{bcolors.OKGREEN}\nShow text-in-file creation status and log? y/n{bcolors.ENDC}")
text_verbose = input('>> ')

if text_verbose == ('y' or 'yes' or 'ye'):
     text_verbose = True
else:
     text_verbose = False

#Setup and print final configuration message

file_num_to_gen = int(file_num_to_gen)
num_to_gen = int(num_to_gen)
bits = int(file_num_to_gen * num_to_gen * (byte_length / 2))

print(f"\n{bcolors.OKGREEN}Ok, generating a total of "+ str(file_num_to_gen) + ' files each containing exactly ' + str(num_to_gen) + ' lines for a total of ' + str(bits) + str(verbose_message))
print(f"{bcolors.ENDC}")

#Create export directory and handle errors, generate export directory work directory

p = Path('Generated Files')
try:
    p.mkdir()
except FileExistsError as exc:
    print(f"{bcolors.FAIL}[ERROR] FileExistsError: ranDum failed to create the export directory, Generated Files already exists.{bcolors.ENDC}")
    print(f"{bcolors.WARNING}[ERROR] Attempting to delete and replace the export folder...{bcolors.ENDC}")
    shutil.rmtree(p, ignore_errors=False, onerror=None)
    print(f"{bcolors.OKGREEN}[SUCCESS] Deleted folder.{bcolors.ENDC}")
    p.mkdir()


export_directory_cd = (os.getcwd() + '\Generated Files')

#Generate compete file path and generate files recursively

for i in range(file_num_to_gen):
     random_title = ('File #' + secrets.token_hex(2))

     if creation_verbose == True:
          print('[Log | Generate] Generating random file name ' + random_title + '.txt')

     completeName = os.path.join(export_directory_cd, random_title + '.txt')

     file = open(completeName, "+w")
     for b in range(num_to_gen):
          current_list_number = str(b)
          password = secrets.token_hex(byte_length)
          file.write(current_list_number + ' | ' + password + '\n')
          
     file.close()