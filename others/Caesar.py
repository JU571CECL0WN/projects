import os
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
       'u', 'v', 'w', 'x', 'y', 'z']
acceptablesigns = ['.', ',', ' ', '?', '!']

def setmode():
    while True:
        mode = input('<E> for Encryption\n<D> for Decryption\n<BF> for Brute Force\nmode: ').lower()
        if mode == 'e':
            return mode
        elif mode == 'd':
            return mode
        elif mode == 'bf':
            return mode
        else:
            print('Is not possible this thing')


def setmsg():
    possible = True
    while True:
        msg = input('Type your message: ').lower()
        for i in msg:
            if i not in abc and i not in acceptablesigns:
                possible = False
        if possible:
            return msg
        else:
            print('Only letters and punctuation signs')

        
def getkey():
    while True:
        key = input('What key do you want? - From number 1 to {0}\nKey:'.format(len(abc) - 1))
        if key.isdigit():
            key = int(key)
            if 1 <= key <= len(abc) - 1:
                return key
            else:
                print('Is not possible this thing')


def encrypt(msg, key):
    wordinprgress = ''
    for i in msg:
        if i in abc:
            index = 0
            for letter in abc:
                if letter == i:
                    if (index + key) < len(abc)-1:
                        wordinprgress += abc[index + key]
                        index -= 1
                    else:
                        wordinprgress += abc[index + key - len(abc)]
                index += 1
        elif i in acceptablesigns:
            wordinprgress += i
    return wordinprgress


def decrypt(msg, key):
    wordinprgress = ''
    for i in msg:
        if i in abc:
            index = 0
            for letter in abc:  
                if letter == i:
                    if (index - key) >= 0:
                        wordinprgress += abc[index - key]
                    else:
                        wordinprgress += abc[index - key + len(abc)]
                index += 1
        elif i in acceptablesigns:
            wordinprgress += i
    return wordinprgress

            
def bruteforce(msg):
    for key in range(1, 26):
        print(decrypt(msg, key))
        

def run():
    os.system('cls')
    mode = setmode()
    msg = setmsg()
    if mode == 'e' or mode == 'd':
        key = getkey()
        os.system('cls')
        if mode == 'e':
            encrypted = encrypt(msg, key)
            print('Your message:\n - {0} - '.format(msg))
            print('Your message encrypted:\n - {0} - '.format(encrypted))
        elif mode == 'd':
            decrypted = decrypt(msg, key)
            print('Your message:\n - {0} - '.format(msg))
            print('Your message decrypted:\n - {0} - '.format(decrypted))
    elif mode == 'bf':
        os.system('cls')
        bruteforce(msg)

        
run()