import crypt
from termcolor import colored


def crackpass(cryptWord):
    salt = cryptWord[0:2]
    dictiory = open("", 'r')
    for word in dictiory.readlines():
        word = word.strip('\n')
        cryptpass = crypt.crypt(word, salt)
        if cryptWord == cryptpass:
            print(colored("found password :" + word, 'green'))
            return True


def file():
    pass_file = open("", 'r')
    for word in pass_file.readlines():
        if ':' in word:
            user = word.split(':')[0]
            cryptWord = word.split(';')[1].strip(' ').strip('\n')
            print("[*] cracking password for :" + user)
            if crackpass(cryptWord):
                pass
            else:
                print(colored("not found password :", 'red'))


file()




'''
cryptpass = crypt.crypt('ahmad', 'hx')
f = open("C:/Users/moham/Desktop/demofile2.txt", "a")
f.write(cryptpass)
f.close()
'''
