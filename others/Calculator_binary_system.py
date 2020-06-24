import os

def mode():
    while True:
        mode = input('<1> for resolve binary system to decimal system\n<2> for resolve decimal system to binary system\n')
        if mode.isdigit():
            mode = int(mode)
            if 0 < mode < 3:
                return mode
            else:
                print('This number is too big or too small')
        else:
            print('This isn\'t a number')


def getnumber(mode):
    while True:
        possible = True
        number = input('What number do you want to resolve?\n')
        if number.isdigit():
            if mode == 1:
                for i in number:
                    if i != '0' and i != '1':
                        possible = False
                if possible:
                    return number
                else:
                    print('ERROR {0}'.format(number))
                    print('This number is not binary')
            elif mode == 2:
                return number
            
            
def resolve_02(number):
    number = int(number)
    result = 0
    elevate = 0
    while True:
        if (2 ** elevate) > number:
            elevate -= 1
            number -= 2 ** elevate
            return number, elevate
        elif (2 ** elevate) == number:
            number -= 2 ** elevate 
            return number, elevate
        else:
            elevate += 1
            
            
def resolve(number, mode):
    if mode == 1:
        result = 0
        for i in range(-1, -len(number) - 1, -1):
            result += int(number[i]) * 2 ** ((-i) - 1)
        return result
    if mode == 2:
        result = 0
        elevates = []
        while True:
            number, elevate = resolve_02(number)
            elevates += [elevate]
            if number == 0:
                break
        if len(elevates) >= 1:
            for i in elevates:
                if i != 0:
                    i -= 1
                    result += int('1' + ('0' * i) + '0')
                else:
                    result += 1
        return result 

    
def run():
    modes = mode()
    number = getnumber(modes)
    difinityresult = resolve(number, modes)
    print(difinityresult)
    
    
run()
