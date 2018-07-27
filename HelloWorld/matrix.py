# streams of strings
# By Casey Key
import random
import os
os.system('color 2E')
wordlist = ['hacker', 'cracker']
wordlist.append(input("Enter a word. "))
while True:
    num = random.randint(33, 254)
    index = random.randint(0, len(wordlist))
    print(chr(num) + wordlist[index] , end='')
