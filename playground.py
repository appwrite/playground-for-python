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
def p(info):
    print("\033[32;1m"+str(info)+"\033[0m")

# Read the docs at https://appwrite.io/docs to get more information
# about API keys and Project IDs
client = Client()
client.set_endpoint('http://YOUR_HOST/v1')
client.set_project('YOUR_PROJECT_ID')
client.set_key('YOU_API_KEY')
client.set_self_signed()
# client.set_jwt('JWT') # Use this to authenticate with JWT instead of API_KEY

collection_id = None
document_id = None
user_id = None
bucket_id = None
file_id = None
document_id = None

def create_collection():
    global collection_id
    database = Database(client)
    p("Running Create Collection API")
    response = database.create_collection(
        collection_id='movies',
        name='Movies',
        permission='document',
        read=['role:all'],
        write=['role:all']
    )
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
    # Wait for attributes to be created
    sleep(2)
    response = database.create_index(
        collection_id,
        key='name_email_idx',
        type="fulltext",
        attributes=['name', 'email']
    )
    print(response)

def list_collections():
    database = Database(client)
    p("Running List Collection API")
    response = database.list_collections()
    print(response)

def get_account():
    account = Account(client)
    p("Running Get Account API");
    response = account.get()
    print(response)


def add_doc():
    global collection_id, document_id
    database = Database(client)
    p("Running Add Document API")
    response = database.create_document(
        collection_id,
        document_id='unique()',
        data={
            'name': "Spider Man",
            'release_year': 1920,
            'rating': 98.5,
            'kids': False
        },
        read=['role:all'],
        write=['role:all']
    )
    document_id = response['$id']
    print(response)

def list_doc():
    global collection_id
    database = Database(client)
    p("Running List Document API")
    response = database.list_documents(collection_id)
    print(response)

def delete_doc():
    global document_id
    database = Database(client)
    p("Running Delete Collection API")
    response = database.delete_document(
        collection_id,
        document_id
    )
    print(response)

def delete_collection():
    global collection_id
    database = Database(client)
    p("Running Delete Collection API")
    response = database.delete_collection(collection_id)
    print(response)

def create_bucket():
    global bucket_id
    storage = Storage(client)
    p("Running Create Bucket API")
    response = storage.create_bucket(
        bucket_id='unique()',
        name='awesome bucket',
        permission='file'
    )
    bucket_id = response['$id']
    print(response)

def upload_file():
    global file_id
    storage = Storage(client)
    p("Running Upload File API")
    response = storage.create_file(
        bucket_id,
        file_id='unique()',
        file="./resources/nature.jpg",
    )
    file_id = response['$id']
    print(response)


def list_files():
    global bucket_id
    storage = Storage(client)
    p("Running List Files API")
    response = storage.list_files(bucket_id)
    print(response)

def delete_file():
    global file_id
    storage = Storage(client)
    p("Running Delete File API")
    response = storage.delete_file(bucket_id, file_id)
    print(response)

def delete_bucket():
    storage = Storage(client)
    p("Running Delete Bucket API")
    response = storage.delete_bucket(bucket_id)
    print(response)

def create_user():
    global user_id
    users = Users(client)
    name = str(randrange(1, maxsize))
    p("Running Create User API")
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
    p("Running List User API")
    response = users.list()
    print(response)

def delete_user():
    global user_id
    users = Users(client)
    p("Running Delete User API")
    response = users.delete(user_id=user_id)
    print(response)

def create_function():
    global function_id
    functions = Functions(client)
    p("Running Create Function API")
    response = functions.create(
        'unique()',
        'Test Function',
        [],
        'python-3.9',
    )
    function_id = response['$id']
    print(response)

def list_function():
    functions = Functions(client)
    p("Running List Function API")
    response = functions.list()
    print(response)

def delete_function():
    global function_id
    functions = Functions(client)
    p("Running Delete Function API")
    response = functions.delete(function_id)
    print(response)

def run_all_tasks():

    # Database
    create_collection()
    list_collections()
    add_doc()
    list_doc()
    delete_doc()
    delete_collection()

    # Storage
    create_bucket()
    upload_file()
    list_files()
    delete_file()
    delete_bucket()

    # Users
    # get_account() # Use this only with JWT
    create_user()
    list_user()
    delete_user()

    # Functions
    create_function()
    list_function()
    delete_function()

if __name__ == "__main__":
    run_all_tasks()
    p("Successfully ran playground!")
