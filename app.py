from appwrite.client import Client
from appwrite.services.users import Users

client = Client()

client.set_endpoint('https://localhost/v1')
client.set_project('5f67b5ada134c') # Your project ID
client.set_key('899b139bdca90746a849f8b31567e378d6e41a0e6667ce5826ce2bbee9caba844b0f5927a61e838d104dfee16c6d411a29b066b7f258ce28f79996f752f8c14ccacb44b7d3f801a8d4047320a8b1011c0332fcc3aedfce4337b8468563a02665ab945b83cefa94cf9922553a1fe7c411314db0c7c9dee2fc36af7e086068b69f') # Your secret API key

users = Users(client)
result = users.create('test@test.com', 'test@123')
