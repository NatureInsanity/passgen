from random import choice, randint, shuffle
import pyperclip
import json


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    return password

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = input('website: ')
    email = input('email: ')
    password = generate_password()
    new_data = {
        website:{
            'email':email,
            'password':password
        }
    }
    if len(website) == 0 or len(password) == 0:
        pass
    else:
        try:
            with open("data.json", "r") as data_file:
                #load data from data.json
                data = json.load(data_file)
        except:
            with open('data.json','w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #update data in data.json
            data.update(new_data)
            with open('data.json','w') as data_file:
                json.dump(data,data_file,indent=4)


        


def load():
    website = input('wich website: ')
    try:
        with open('data.json','r') as data_file:
            data = json.load(data_file)
            print(data[website]['email'])
            print(data[website]['password'])

    except:
        save()

want = input('what do you want? save/load?: ')

if want == 'save':
    save()
elif want == 'load':
    load()
else:
    print('error, wrong input')