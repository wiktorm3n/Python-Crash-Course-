import json

def get_new_username():
    '''Prompt for new username'''
    username = input("What is your name? : ")
    filename = 'username.json'
    with open(filename,'w') as f:
        json.dump(username,f)
    return username 

def greet_user():
    '''Greet user by name'''
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? : ")
        with open(filename,'w') as f:
            json.dump(username,f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        is_this_correct_user = input(f"Are you {username}?\nIf no enter 'no', otherwise just enter any key.\n")
        if is_this_correct_user == 'no':
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")

        else:
            print(f"Welcome back, {username}!")
      
def get_stored_username():
    '''Get stored username if avaible'''
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

greet_user()
