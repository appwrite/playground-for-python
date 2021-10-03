import urllib3

from appwrite.client import Client
from appwrite.services.users import Users
from appwrite.services.database import Database
from appwrite.services.storage import Storage
from appwrite.services.account import Account

import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Helper method to print green colored output.
def print_green(prt):
    print("\033[32;1m"+str(prt)+"\033[0m")

    
# Config

# Read the docs at https://appwrite.io/docs to get more information
# about API keys and Project IDs
ENDPOINT = 'https://localhost/v1'
PROJECT_ID = '<Project ID>'
API_KEY = '<Secret API Key>'

client = Client()

client.set_endpoint(ENDPOINT)
client.set_project(PROJECT_ID)
client.set_key(API_KEY)
# client.set_jwt('JWT') # Use this to authenticate with JWT instead of API_KEY


collectionId = None
userId = None


# API Calls
#   - api.create_collection
#   - api.list_collection
#   - api.add_doc
#   - api.list_doc
#   - api.upload_file
#   - api.list_files
#   - api.delete_file
#   - api.create_user
#   - api.list_user
#   - api.get_account # Work only with JWT

# List of API definitions

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


def get_account():
    account = Account(client)
    print_green("Running Get Account API");
    response = account.get()
    print(response)


def  add_doc():
     database = Database(client)
     print_green("Running Add Document API")
     response = database.create_document(
         collectionId,
         {
             'name': "Spider Man",
             'release_year': 1920,
         }
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


def list_files():
    storage = Storage(client)
    print_green("Running List Files API")
    result = storage.list_files()
    file_count = result['sum']
    print("Total number of files {} ".format(file_count))
    files = result['files']
    print(files)


def delete_file():
    storage = Storage(client)
    print_green("Running Delete File API")
    result = storage.list_files()
    first_file_id = result['files'][0]['$id']
    response = storage.delete_file(first_file_id)
    print(response)


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
    list_files()
    delete_file()
    create_user(
        name + '@test.com',
        name + '@123',
        name
    )
    list_user()
    # get_account() # works only with JWT


if __name__ == "__main__":

    run_all_tasks()
    print_green("Successfully Ran playground!")
