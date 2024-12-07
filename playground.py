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
from appwrite.permission import Permission
from appwrite.role import Role
from appwrite.id import ID


# Helper method to print green colored output.
def p(info):
    print("\033[32;1m" + str(info) + "\033[0m")


# Read the docs at https://appwrite.io/docs to get more information
# about API keys and Project IDs
client = (client
  .set_endpoint('https://cloud.appwrite.io/v1') # Appwrite cloud platform API Endpoint
  .set_project('YOUR_PROJECT_ID') # Replace with your appwrite cloud project ID
  .set_key('YOU_API_KEY') # Replace with your appwrite cloud project api key
  .set_self_signed() # Use only on dev mode with a self-signed SSL cert
)

# client.set_jwt('JWT') # Use this to authenticate with JWT instead of API_KEY

databases = Databases(client)
storage = Storage(client)
functions = Functions(client)
users = Users(client)

database_id = None
collection_id = None
document_id = None
user_id = None
bucket_id = None
file_id = None
document_id = None
function_id = None
deployment_id = None
execution_id = None


def create_database():
    global database_id

    p("Running Create Database API")
    response = databases.create(
        database_id=ID.unique(),
        name="Movies",
    )
    database_id = response["$id"]
    print(response)


def create_collection():
    global collection_id

    p("Running Create Collection API")
    response = databases.create_collection(
        database_id,
        collection_id=ID.unique(),
        name="Movies",
        document_security=True,
        permissions=[
            Permission.read(Role.any()),
            Permission.create(Role.users()),
            Permission.update(Role.users()),
            Permission.delete(Role.users()),
        ],
    )

    collection_id = response["$id"]
    print(response)

    response = databases.create_string_attribute(
        database_id,
        collection_id,
        key="name",
        size=255,
        required=True,
    )
    print(response)

    response = databases.create_integer_attribute(
        database_id, collection_id, key="release_year", required=True, min=0, max=9999
    )
    print(response)

    response = databases.create_float_attribute(
        database_id, collection_id, key="rating", required=True, min=0.0, max=99.99
    )
    print(response)

    response = databases.create_boolean_attribute(
        database_id, collection_id, key="kids", required=True
    )
    print(response)

    response = databases.create_email_attribute(
        database_id, collection_id, key="email", required=False
    )
    print(response)

    # Wait for attributes to be created
    sleep(2)

    response = databases.create_index(
        database_id,
        collection_id,
        key="name_email_idx",
        type="fulltext",
        attributes=["name", "email"],
    )
    print(response)


def list_collections():
    p("Running List Collection API")
    response = databases.list_collections(database_id)
    print(response)


def get_account():
    account = Account(client)
    p("Running Get Account API")
    response = account.get()
    print(response)


def add_doc():
    global document_id

    p("Running Add Document API")
    response = databases.create_document(
        database_id,
        collection_id,
        document_id=ID.unique(),
        data={
            "name": "Spider Man",
            "release_year": 1920,
            "rating": 98.5,
            "kids": False,
        },
        permissions=[
            Permission.read(Role.users()),
            Permission.update(Role.users()),
            Permission.delete(Role.users()),
        ],
    )
    document_id = response["$id"]
    print(response)


def list_doc():
    p("Running List Document API")
    response = databases.list_documents(database_id, collection_id)
    print(response)


def delete_doc():
    p("Running Delete Database API")
    response = databases.delete_document(database_id, collection_id, document_id)
    print(response)


def delete_collection():
    p("Running Delete Collection API")
    response = databases.delete_collection(database_id, collection_id)
    print(response)


def delete_database():
    p("Running Delete Database API")
    response = databases.delete(database_id)
    print(response)


def create_bucket():
    global bucket_id

    p("Running Create Bucket API")
    response = storage.create_bucket(
        bucket_id=ID.unique(),
        name="awesome bucket",
        file_security=True,
        permissions=[
            Permission.read(Role.any()),
            Permission.create(Role.users()),
            Permission.update(Role.users()),
            Permission.delete(Role.users()),
        ],
    )
    bucket_id = response["$id"]
    print(response)


def list_buckets():
    p("Running List Buckets API")
    response = storage.list_buckets()
    print(response)


def upload_file():
    global file_id

    p("Running Upload File API")
    response = storage.create_file(
        bucket_id,
        file_id=ID.unique(),
        file=InputFile.from_path("./resources/nature.jpg"),
    )
    file_id = response["$id"]
    print(response)


def list_files():
    p("Running List Files API")
    response = storage.list_files(bucket_id)
    print(response)


def delete_file():
    p("Running Delete File API")
    response = storage.delete_file(bucket_id, file_id)
    print(response)


def delete_bucket():
    p("Running Delete Bucket API")
    response = storage.delete_bucket(bucket_id)
    print(response)


def create_user():
    global user_id

    name = str(randrange(1, maxsize))
    p("Running Create User API")
    response = users.create(
        user_id=ID.unique(), email=f"{name}@test.com", password=f"{name}@123", name=name
    )
    user_id = response["$id"]
    print(response)


def list_user():
    p("Running List User API")
    response = users.list()
    print(response)


def delete_user():
    p("Running Delete User API")
    response = users.delete(user_id)
    print(response)


def create_function():
    global function_id

    p("Running Create Function API")
    response = functions.create(
        function_id=ID.unique(),
        name="Test Function",
        execute=[Role.any()],
        runtime="python-3.9",
    )
    function_id = response["$id"]
    print(response)


def list_function():
    p("Running List Function API")
    response = functions.list()
    print(response)


def delete_function():
    p("Running Delete Function API")
    response = functions.delete(function_id)
    print(response)


def create_deployment():
    global function_id
    global deployment_id

    p("Running Create Deployment API")
    response = functions.create_deployment(
        function_id,
        code=InputFile.from_path("./resources/code.tar.gz"),
        activate=True,
        entrypoint="main.py",
    )

    deployment_id = response["$id"]
    print(response)


def list_deployments():
    global function_id

    p("Running List Deployments API")
    response = functions.list_deployments(function_id)
    print(response)


def delete_deployment():
    global function_id
    global deployment_id

    p("Running Delete Deployment API")
    response = functions.delete_deployment(function_id, deployment_id)
    print(response)


def create_execution():
    global function_id
    global execution_id

    p("Running Create Execution API")
    response = functions.create_execution(function_id)

    execution_id = response["$id"]

    print(response)


def list_executions():
    global function_id

    p("Running List Executions API")
    response = functions.list_executions(function_id)
    print(response)


def delete_execution():
    global function_id
    global execution_id

    p("Running Delete Execution API")
    response = functions.delete_execution(function_id, execution_id)
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
    create_deployment()
    list_deployments()
    create_execution()
    list_executions()
    delete_execution()
    delete_deployment()
    delete_function()


if __name__ == "__main__":
    run_all_tasks()
    p("Successfully ran playground!")