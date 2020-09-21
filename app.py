from appwrite.client import Client
from appwrite.services.users import Users
from appwrite.services.database import Database

# Config

ENDPOINT = 'https://localhost/v1'
PROJECT_ID = '5f67b5ada134c'
API_KEY = '899b139bdca90746a849f8b31567e378d6e41a0e6667ce5826ce2bbee9caba844b0f5927a61e838d104dfee16c6d411a29b066b7f258ce28f79996f752f8c14ccacb44b7d3f801a8d4047320a8b1011c0332fcc3aedfce4337b8468563a02665ab945b83cefa94cf9922553a1fe7c411314db0c7c9dee2fc36af7e086068b69f'

client = Client()

client.set_endpoint(ENDPOINT)
client.set_project(PROJECT_ID)
client.set_key(API_KEY)

users = Users(client)
result = users.create('test@test.com', 'test@123')

collectionId = None
userId = None

# List of API definations

async def createCollection():
    database = Database(client)
    print("Running Create Collection API")
    response = await database.create_collection(
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
    collectionId = response.id
    print(response)


async def listCollection():
    database = Database(client)
    print("Running List Collection API")
    response = await database.list_collections()
    collection = response.collections[0]
    print(collection)

