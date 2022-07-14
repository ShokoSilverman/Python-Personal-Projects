from pymongo import MongoClient
from Imports.Silver_ODBC import MongoDB as Silver_MongoDB

# myclient = MongoClient('mongodb+srv://SimonSilverman:SimonsPassWord@cluster0.wexky.mongodb.net/TestAtlas?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE')
# mydb = myclient.TestAtlas
# mycol = mydb.TestAtlasDB

mongo = Silver_MongoDB('localhost',27017, 'hospital')


def cont():
    going = input("would you like to add another field? (Yes/No): ")
    if going.lower() == 'yes':
        return True
    elif going.lower() == 'no':
        return False
    else:
        print('You must enter Yes or No!')
        cont()

def add_to_db():
    in_dict = {}

    keep_looping = True
    while keep_looping:
        key = input("enter a key: ")
        value = input("enter a value: ")
        in_dict[key] = value

        keep_looping = cont()

    mongo.insert_one('procedureNotes', in_dict)
    print('entry added!')

while True:
    add_to_db()
    next = input('would you like to add another entry? ')
    if next != 'Y' or next != 'y':
        break


