while True:
    try:
        print('Enter number:') #this prints a command for people to enter a number (works)
        number = int(input()) #this asks people to enter a number (works)
    except ValueError:
        print('please enter a numeric value.')

    else:
        break

def collatz(): #define collatz function (works)

    global number

    if number % 2 == 0:
        number = number // 2
        print(number)

    elif number % 2 == 1:
        number = number * 3 + 1
        print(number)
    
while number != 1: #ensures program keeps working until it evaluates to "1"
    collatz()
    continue












