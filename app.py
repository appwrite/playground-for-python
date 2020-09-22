from appwrite.client import Client
from appwrite.services.users import Users
from appwrite.services.database import Database
from appwrite.services.storage import Storage

import datetime

# Helper method to print green colored output.
def print_green(prt):
    print("\033[32;1m"+str(prt)+"\033[0m")

# Config

ENDPOINT = 'https://localhost/v1'
PROJECT_ID = '5f69ba7d23216'
API_KEY = 'e8648fb26ea100a1ddca908adb2802a73081243621f7a228435e4b84b8aa1f25a9355af571e0c9c29c8b4840e129aa4160ea43194bd6620fc4520828becd243be25b332cd91c68d1a21a5171a079828e006321060b416189ec7814d0df2d4eb961f39b2ba5de51e6bd69ab8ccf1722f97e9aca86596b0d65247720917411b83e'

client = Client()

client.set_endpoint(ENDPOINT)
client.set_project(PROJECT_ID)
client.set_key(API_KEY)

collectionId = None
userId = None

# API Calls
#   - api.create_collection
#   - api.list_collection
#   - api.add_doc
#   - api.list_doc
#   - api.upload_file
#   - api.create_user
#   - api.list_user

# List of API definations

def create_collection():
    global collectionId
    database = Database(client)
    print_green("Running Create Collection API")
    response = database.create_collection(
        'Movies',
        ['*'],
        ['*'],
        [
            {'label': "Name", 'key': "name", 'type': "text",
             'default': "Empty Name", 'required': True, 'array': False},
            {'label': 'release_year', 'key': 'release_year', 'type': 'numeric',
             'default': 1970, 'required': True, 'array': False}
        ]
    )
    collectionId = response['$id']
    print(response)


def list_collection():
    database = Database(client)
    print_green("Running List Collection API")
    response = database.list_collections()
    collection = response['collections'][0]
    print(collection)


def add_doc():
    database = Database(client)
    print_green("Running Add Document API")
    response = database.create_document(
        collectionId,
        {
            'name': "Spider Man",
            'release_year': 1920,
        },
        ['*'],
        ['*']
    )
    print(response)


def list_doc():
    database = Database(client)
    print_green("Running List Document API")
    response = database.list_documents(collectionId)
    print(response)


def upload_file():
    storage = Storage(client)
    print_green("Running Upload File API")
    response = storage.create_file(
        open("./nature.jpg", 'rb'),
        [],
        []
    )


def create_user(email, password, name):
    global userId
    users = Users(client)
    print_green("Running Create User API")
    response = users.create(
        email,
        password,
        name
    )
    userId = response['$id']
    print(response)


def list_user():
    users = Users(client)
    print_green("Running List User API")
    response = users.list()
    print(response)


def run_all_tasks():

    name = str(datetime.datetime.now()).split()[0]

    create_collection()
    list_collection()
    add_doc()
    list_doc()
    upload_file()
    create_user(
        name + '@test.com',
        name + '@123',
        name
    )
    list_user()


if __name__ == "__main__":

    run_all_tasks()
    print_green("Successfully Ran playground!")
