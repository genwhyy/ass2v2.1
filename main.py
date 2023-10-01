from account import UserAccount
from authsystem import AuthSystem

def main():
    system = AuthSystem('users.json')

    while True: 
        print(f'Hello! What do you want to do?\n1.Sign up\n2.Sign in\n3.Cancel')
        answer = int(input('Enter your choice here: '))

        if (answer == 1):
            print('Enter your personal information')
            name = input('YOUR NAME: ')
            surname = input('YOUR SURNAME: ')
            age = input('YOUR AGE: ')
            password = input('CREATE A PASSWORD: ')
            account = UserAccount(name, surname, age, password)
            if system.sign_up(account):
                print('SUCCES!')
            else:
                print('ACCOUNT ALREADY EXISTS')

        if (answer == 2):
            username = input('Enter your USERNAME: ')
            password = input('Enter your PASSWORD: ')
            if system.auth_acc(username, password): 
                print('SUCCESS!')
            else:
                print('Something went WRONG! Try again.')

        if (answer == 3):
            print(f'\n')
            print('Goodbye!')
            break

        else: print('I do not understand, try again! ')

if __name__ == '__main__':
    main()