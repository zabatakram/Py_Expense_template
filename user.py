from PyInquirer import prompt
from csv import reader, writer
user_questions = [
    {
        "type": "input",
        "name": "name",
        "message": "New User - Name: ",
    }
]


def getUsersList():
    with open("users.csv", "r") as csv:
        users = reader(csv)
        res = []
        for user in users:
            res.append({'name': user[0]})
        return res

def add_user():
    userFileNameW = open("users.csv", "a")
    userFileNameR = open("users.csv", "r")
    usersReader = reader(userFileNameR)
    usersWriter = writer(userFileNameW)

    name = prompt(user_questions)["name"]
    # See if user already exists
    for user in usersReader:
        if user[0].lower() == name.lower():
            print("User " + name + " already exists !")
            userFileNameR.close()
            userFileNameW.close()
            return False
    # Spaces not allowed
    if ' ' in name:
        print("Spaces are not allowed !")
        return add_user()
    # Add User
    usersWriter.writerow([name])
    print("User " + name + " added !")
    userFileNameR.close()
    userFileNameW.close()
    return True
