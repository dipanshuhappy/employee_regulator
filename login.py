def read_file():
    with open("users.txt") as file:
        return file.read()
def read_lines():
    with open("users.txt") as file:
        return [line.strip() for line in file.readlines()]
def get_users():
    users=[]
    for user in read_lines():
        username=user.split(" ")[0]
        users.append(username)
    return users
def does_user_exist(username):
    try:
        get_users().index(username)
    except ValueError:
        return False
    else:
        return True
def is_password_valid(username,password_input):
    is_valid=False
    for user in read_lines():
        username_read=user.split(" ")[0]
        if username_read==username:
            password=user.split(" ")[1]
            if password_input.strip()==password.strip():
                is_valid=True
                break
    return is_valid
            


