name = input('Hello, what is your name? ')
random_int = int(input('Enter a number 1-100: '))

if random_int > 100 or random_int < 1:
    print('Your entry is invalid')
    random_int = int(input('Enter a number between 1-100: '))
while random_int <= 100 or random_int >= 1:
    if random_int % 2 == 1 and random_int < 60:
        print(name + ' you entered ' + str(random_int) + ' and it is odd and less than 60')
    elif random_int % 2 == 0 and 24 >+ random_int >= 2:
        print(name + ' your number is even and less than 25')
    elif random_int % 2 == 0 and 60 >= random_int >=26:
        print(name + ' your number is even and between 26 and 60 inclusive')
    elif random_int % 2 == 0 and random_int > 60:
        print(name + ' your number is even and greater than 60')
    elif random_int % 2 == 1 and random_int > 60:
        print(name + ' you entered ' + str(random_int) + ' and it is odd and greater than 60')
    break
