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

class Create:
    def create_database():
        """
        It creates a database called 'Movies' in the Azure Cosmos DB account
        """
        global database_id
        databases = Databases(client, 'moviesDB')
        p("Running Create Database API")
        response = databases.create(
            name='Movies',
        )
        database_id = response['$id']
        print(response)

    def create_collection():
        """
        Create a collection called `movies` with a few attributes and an index
        """
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

    def create_bucket():
        """
        `create_bucket()` creates a bucket with the name `awesome bucket` and the permission `file`
        """
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
    
    def create_user():
        """
        > Create a user with a random name and email address
        """
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

    def create_function():
        """
        Create a function called 'unique()' that takes no arguments and returns a unique value
        """
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

class Delete:
    def delete_doc():
        """
        Delete a document from a collection
        """
        global database_id, collection_id, document_id
        databases = Databases(client, database_id)
        p("Running Delete Collection API")
        response = databases.delete_document(
            collection_id,
            document_id
        )
        print(response)
    
    def delete_collection():
        """
        > This function deletes the collection with the specified id
        """
        global database_id, collection_id
        databases = Databases(client, database_id)
        p("Running Delete Collection API")
        response = databases.delete_collection(collection_id)
        print(response)
    
    def delete_database():
        """
        This function deletes the database that was created in the previous function
        """
        global database_id
        databases = Databases(client, database_id)
        p("Running Delete Database API")
        response = databases.delete()
        print(response)
    
    def delete_file():
        """
        It deletes the file with the given file_id from the bucket with the given bucket_id.
        """
        global file_id
        storage = Storage(client)
        p("Running Delete File API")
        response = storage.delete_file(bucket_id, file_id)
        print(response)

    def delete_bucket():
        """
        > Delete a bucket
        """
        storage = Storage(client)
        p("Running Delete Bucket API")
        response = storage.delete_bucket(bucket_id)
        print(response)

    def delete_user():
        """
        It deletes the user with the user_id that was created in the previous function.
        """
        global user_id
        users = Users(client)
        p("Running Delete User API")
        response = users.delete(user_id=user_id)
        print(response)

    def delete_function():
        """
        > Delete a function
        """
        global function_id
        functions = Functions(client)
        p("Running Delete Function API")
        response = functions.delete(function_id)
        print(response)

class List:

    def list_collections():
        """
        This function lists all the collections in the database
        """
        global database_id
        databases = Databases(client, database_id)
        p("Running List Collection API")
        response = databases.list_collections()
        print(response)

    def list_doc():
        """
        > This function lists all documents in a collection
        """
        global database_id, collection_id
        databases = Databases(client, database_id)
        p("Running List Document API")
        response = databases.list_documents(collection_id)
        print(response)

    def list_buckets():
        """
        > This function lists all the buckets in the project
        """
        storage = Storage(client)
        p("Running List Buckets API")
        response = storage.list_buckets()
        print(response)
    
    def list_files():
        """
        > List all files in a bucket
        """
        global bucket_id
        storage = Storage(client)
        p("Running List Files API")
        response = storage.list_files(bucket_id)
        print(response)
    
    def list_user():
        """
        `users.list()`
        """
        users = Users(client)
        p("Running List User API")
        response = users.list()
        print(response)

    def list_function():
        """
        It lists all the functions in the account.
        """
        functions = Functions(client)
        p("Running List Function API")
        response = functions.list()
        print(response)

class Other:

    def get_account():
        """
        > This function gets the account information for the account associated with the API key
        """
        account = Account(client)
        p("Running Get Account API");
        response = account.get()
        print(response)

    def add_doc():
        """
        > Create a document with the given data and permissions
        """
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

    def upload_file():
        """
        Uploads a file to the bucket.
        """
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



def run_all_tasks():

    # Databases
    Create.create_database()
    Create.create_collection()
    List.list_collections()
    Other.add_doc()
    List.list_doc()
    Delete.delete_doc()
    Delete.delete_collection()
    Delete.delete_database()

    # Storage
    Create.create_bucket()
    List.list_buckets()
    Other.upload_file()
    List.list_files()
    Delete.delete_file()
    Delete.delete_bucket()

    # Users
    # get_account() # Use this only with JWT
    Create.create_user()
    List.list_user()
    Delete.delete_user()

    # Functions
    Create.create_function()
    List.list_function()
    Delete.delete_function()

if __name__ == "__main__":
# Calling the function `run_all_tasks()` and printing the message `Successfully ran playground!`
    run_all_tasks()
    p("Successfully ran playground!")
