
file_path = 'C:/Users/SAGAR/Desktop/passwords.txt'


passwords = {}
with open(file_path, 'r') as file:
    for line in file:
        parts = line.strip().split(' : ')
        passwords[parts[0]] = parts[1]

print('welcome To The Password Manager!')
print('Please Select an Option')
print('(1) Add Password')
print('(2) View Websites')
print('(3) Search Password')
print('(4) Update Password')
print('(5) Remove Password')
print('(6) Exit')
choice = int(input('Enter your choice:- '))

#Encryption
def encrypt(text):
    encrypted = ''
    for char in text:
        new = ord(char)
        new_char_n = new - 97
        new_char_pos = new_char_n + 10
        new_char_pos = new_char_pos % 26
        new_char = chr(new_char_pos + 97)
        encrypted += new_char
    return encrypted

#Decryption
def decrypt(text):
    decrypted = ''
    for char in text:
        new = ord(char)
        new_char_n = new - 97
        new_char_pos = new_char_n - 10
        new_char_pos = new_char_pos % 26
        new_char = chr(new_char_pos + 97)
        decrypted += new_char
    return decrypted

def add_password():
    add_website = input('Enter The Website Address:- ')
    add_pass = input('Enter The Password Of the Website:- ')
    with open(file_path, 'a') as file:
        encrypted_pass = encrypt(add_pass)
        file.write(f'{add_website} : {encrypted_pass}\n')
    passwords[add_website] = encrypted_pass
    print('Password Added Successfully!')
    choice = int(input('Enter your choice:- '))
    return choice

def view_websites():
    if passwords == {}:
        print("No Websites Added Yet!!")
        choice = int(input('Enter your choice:- '))
        return choice

    else:
        for key in passwords:
            print(key)
        choice = int(input('Enter your choice:- '))
        return choice

def search_password():
    if passwords == {}:
        print("No Passwords Added Yet!!")
        choice = int(input('Enter your choice:- '))
        return choice
    else:
        search_web = input('What Website Password are you Looking For? :- ')
        if search_web in passwords:
            print(search_web, decrypt(passwords[search_web]))
            choice = int(input('Enter your choice:- '))
            return choice
        else:
            print('No Such Website Added Yet!')
            choice = int(input('Enter your choice:- '))
            return choice

def update_password():
    if passwords == {}:
        print("No Passwords Added Yet!!")
        choice = int(input('Enter your choice:- '))
        return choice
    else:
        update_website = input('Enter the Website Whose Password You Want To Update:- ')
        if update_website in passwords:
            new_password = input('Enter the new Password:- ')
            passwords[update_website] = encrypt(new_password)
            with open(file_path, 'w') as file:
                for website in passwords:
                    file.write(f'{website} : {passwords[website]}' '\n')
            print('Password Updated Successfully!')
            choice = int(input('Enter your choice:- '))
            return choice
        else:
            print('No Such Website Added Yet!')
            choice = int(input('Enter your choice:- '))
            return choice

def remove_password():
    if passwords == {}:
        print("No Passwords Added Yet!!")
        choice = int(input('Enter your choice:- '))
        return choice
    else:
        remove_password = input('Enter the website whose Password You Want To Remove:- ')
        if remove_password in passwords:
            passwords.pop(remove_password)
            with open(file_path, 'w') as file:
                for website in passwords:
                    file.write(f'{website} : {passwords[website]}' '\n')
            print('Password Removed Successfully!')
            choice = int(input('Enter your choice:- '))
            return choice
        else:
            print('No Such Password Added Yet!')
            choice = int(input('Enter your choice:- '))
            return choice

while choice != 6:
    if choice == 1:
       choice = add_password()

    elif choice == 2:
       choice = view_websites()

    elif choice == 3:
        choice = search_password()

    elif choice == 4:
        choice = update_password()

    elif choice == 5:
        choice = remove_password()

print('Thank You!')