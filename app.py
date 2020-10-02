from appwrite.client import Client
from appwrite.services.users import Users
from appwrite.services.database import Database
from appwrite.services.storage import Storage

import asyncio
import datetime

# Helper method to print green colored output.
def print_green(prt):
    print("\033[32;1m"+str(prt)+"\033[0m")

# Config

ENDPOINT = 'https://localhost/v1'
PROJECT_ID = '<Project ID>'
API_KEY = '<Secret API Key>'

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

async def create_collection():
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


async def list_collection():
    database = Database(client)
    print_green("Running List Collection API")
    response = database.list_collections()
    collection = response['collections'][0]
    print(collection)


async def add_doc():
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


async def list_doc():
    database = Database(client)
    print_green("Running List Document API")
    response = database.list_documents(collectionId)
    print(response)


async def upload_file():
    storage = Storage(client)
    print_green("Running Upload File API")
    response = storage.create_file(
        open("./nature.jpg", 'rb'),
        [],
        []
    )


async def create_user(email, password, name):
    users = Users(client)
    print_green("Running Create User API")
    response = users.create(
        email,
        password,
        name
    )
    userId = response['$id']
    print(response)


async def list_user():
    users = Users(client)
    print_green("Running List User API")
    response = users.list()
    print(response)


async def run_all_tasks():

    name = str(datetime.datetime.now()).split()[0]

    await create_collection()
    await list_collection()
    await add_doc()
    await list_doc()
    await upload_file()
    await create_user(
        name + '@test.com',
        name + '@123',
        name
    )
    await list_user()


if __name__ == "__main__":

    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run_all_tasks())
        loop.close()
    except Exception as e:
        print(e)
    else:
        print_green("Successfully Ran playground!")
