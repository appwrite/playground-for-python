from time import sleep
from random import randrange
from sys import maxsize

from appwrite.client import Client
from appwrite.services.users import Users
from appwrite.services.databases import Databases
from appwrite.services.storage import Storage
from appwrite.services.account import Account
from appwrite.services.functions import Functions
from appwrite.input_file import InputFile

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

database_id = None
collection_id = None
document_id = None
user_id = None
bucket_id = None
file_id = None
document_id = None

def create_database():
    global database_id
    databases = Databases(client, 'moviesDB')
    p("Running Create Database API")
    response = databases.create(
        name='Movies',
    )
    database_id = response['$id']
    print(response)

def create_collection():
    global collection_id, database_id
    databases = Databases(client, database_id)
    p("Running Create Database API")
    response = databases.create_collection(
        collection_id='movies',
        name='Movies',
        permission='document',
        read=['role:all'],
        write=['role:all']
    )
    collection_id = response['$id']
    print(response)
    response = databases.create_string_attribute(
        collection_id,
        key='name',
        size=255,
        required=True,
    )
    print(response)
    response = databases.create_integer_attribute(
        collection_id,
        key='release_year',
        required=True,
        min=0,
        max=9999
    )
    print(response)
    response = databases.create_float_attribute(
        collection_id,
        key='rating',
        required=True,
        min=0.0,
        max=99.99
    )
    print(response)
    response = databases.create_boolean_attribute(
        collection_id,
        key='kids',
        required=True
    )
    print(response)
    response = databases.create_email_attribute(
        collection_id,
        key='email',
        required=False,
        default=""
    )
    print(response)
    # Wait for attributes to be created
    sleep(2)
    response = databases.create_index(
        collection_id,
        key='name_email_idx',
        type="fulltext",
        attributes=['name', 'email']
    )
    print(response)

def list_collections():
    global database_id
    databases = Databases(client, database_id)
    p("Running List Collection API")
    response = databases.list_collections()
    print(response)

def get_account():
    account = Account(client)
    p("Running Get Account API");
    response = account.get()
    print(response)


def add_doc():
    global database_id, collection_id, document_id
    databases = Databases(client, database_id)
    p("Running Add Document API")
    response = databases.create_document(
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
    global database_id, collection_id
    databases = Databases(client, database_id)
    p("Running List Document API")
    response = databases.list_documents(collection_id)
    print(response)

def delete_doc():
    global database_id, collection_id, document_id
    databases = Databases(client, database_id)
    p("Running Delete Collection API")
    response = databases.delete_document(
        collection_id,
        document_id
    )
    print(response)

def delete_collection():
    global database_id, collection_id
    databases = Databases(client, database_id)
    p("Running Delete Collection API")
    response = databases.delete_collection(collection_id)
    print(response)

def delete_database():
    global database_id
    databases = Databases(client, database_id)
    p("Running Delete Database API")
    response = databases.delete()
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

def list_buckets():
    storage = Storage(client)
    p("Running List Buckets API")
    response = storage.list_buckets()
    print(response)

def upload_file():
    global file_id
    storage = Storage(client)
    p("Running Upload File API")
    response = storage.create_file(
        bucket_id,
        file_id='unique()',
        file=InputFile.from_path("./resources/nature.jpg"),
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

    # Databases
    create_database()
    create_collection()
    list_collections()
    add_doc()
    list_doc()
    delete_doc()
    delete_collection()
    delete_database()

    # Storage
    create_bucket()
    list_buckets()
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
