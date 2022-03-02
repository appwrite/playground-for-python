from time import sleep
from random import randrange
from sys import maxsize

from appwrite.client import Client
from appwrite.services.users import Users
from appwrite.services.database import Database
from appwrite.services.storage import Storage
from appwrite.services.account import Account
from appwrite.services.functions import Functions

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
client.set_self_signed()
# client.set_jwt('JWT') # Use this to authenticate with JWT instead of API_KEY

collection_id = None
user_id = None
bucket_id = None
file_id = None

# API Calls
#   - api.create_collection
#       - api.create_string_attribute
#       - api.create_integer_attribute
#       - api.create_float_attribute
#       - api.create_boolean_attribute
#       - api.create_email_attribute
#       - api.create_index
#   - api.list_collection
#   - api.add_doc
#   - api.list_doc
#   - api.upload_file
#   - api.list_files
#   - api.delete_file
#   - api.create_user
#   - api.list_user
#   - api.get_account # Work only with JWT
#   - api.create_function
#   - api.list_function
#   - api.delete_function

# List of API definitions

def create_collection():
    database = Database(client)
    print_green("Running Create Collection API")
    response = database.create_collection(
        'movies',
        'Movies',
        'document',
        ['role:all'],
        ['role:all']
    )
    global collection_id
    collection_id = response['$id']
    print(response)
    response = database.create_string_attribute(
        collection_id,
        key='name',
        size=255,
        required=True,
    )
    print(response)
    response = database.create_integer_attribute(
        collection_id,
        key='release_year',
        required=True,
        min=0,
        max=9999
    )
    print(response)
    response = database.create_float_attribute(
        collection_id,
        key='rating',
        required=True,
        min=0.0,
        max=99.99
    )
    print(response)
    response = database.create_boolean_attribute(
        collection_id,
        key='kids',
        required=True
    )
    print(response)
    response = database.create_email_attribute(
        collection_id,
        key='email',
        required=False,
        default=""
    )
    print(response)
    sleep(2)
    response = database.create_index(
        collection_id,
        key='name_email_idx',
        type="fulltext",
        attributes=['name', 'email']
    )
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


def add_doc():
    database = Database(client)
    global collection_id
    print_green("Running Add Document API")
    response = database.create_document(
        collection_id,
        'unique()',
        {
            'name': "Spider Man",
            'release_year': 1920,
            'rating': 98.5,
            'kids': False
        },
        ['role:all'],
        ['role:all']
    )
    print(response)

def list_doc():
    database = Database(client)
    print_green("Running List Document API")
    response = database.list_documents(collection_id)
    print(response)

def delete_collection():
    database = Database(client)
    print_green("Running Delete Collection API")
    response = database.delete_collection(collection_id)
    print(response)

def create_bucket():
    global bucket_id
    storage = Storage(client)
    print_green("Running Create Bucket API")
    response = storage.create_bucket(
        'unique()',
        'awesome bucket',
        'file'
    )
    bucket_id = response['$id']
    print(response)

def upload_file():
    storage = Storage(client)
    print_green("Running Upload File API")
    response = storage.create_file(
        bucket_id,
        'unique()',
        "./resources/nature.jpg",
    )
    print(response)


def list_files():
    storage = Storage(client)
    print_green("Running List Files API")
    result = storage.list_files(bucket_id)
    file_count = result['total']
    print("Total number of files {} ".format(file_count))
    files = result['files']
    print(files)

def delete_file():
    storage = Storage(client)
    print_green("Running Delete File API")
    result = storage.list_files(bucket_id)
    first_file_id = result['files'][0]['$id']
    response = storage.delete_file(bucket_id, first_file_id)
    print(response)

def delete_bucket():
    storage = Storage(client)
    print_green("Running Delete Bucket API")
    response = storage.delete_bucket(bucket_id)
    print(response)

def create_user():
    users = Users(client)
    name = str(randrange(1, maxsize))
    print_green("Running Create User API")
    response = users.create(
        'unique()',
        f'{name}@test.com',
        f'{name}@123',
        name
    )
    user_id = response['$id']
    print(response)

def list_user():
    users = Users(client)
    print_green("Running List User API")
    response = users.list()
    print(response)

def create_function():
    global function_id
    functions = Functions(client)
    print_green("Running Create Function API")
    response = functions.create(
        'unique()',
        'Test Function',
        [],
        'python-3.10',
    )
    function_id = response['$id']
    print(response)

def list_function():
    functions = Functions(client)
    print_green("Running List Function API")
    response = functions.list()
    print(response)

def delete_function():
    functions = Functions(client)
    print_green("Running Delete Function API")
    response = functions.delete(function_id)
    print(response)

def run_all_tasks():
    create_collection()
    list_collection()
    add_doc()
    list_doc()
    delete_collection()
    create_bucket()
    upload_file()
    list_files()
    delete_file()
    delete_bucket()
    create_user()
    list_user()
    create_function()
    list_function()
    delete_function()
    # get_account() # works only with JWT

if __name__ == "__main__":
    run_all_tasks()
    print_green("Successfully ran playground!")
