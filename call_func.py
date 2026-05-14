#!/usr/bin/env python3

from appwrite.client import Client
from appwrite.services.functions import Functions
from appwrite.enums.execution_method import ExecutionMethod

client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1')
client.set_project('6694e3a700362a755942')
# client.set_key('0e3786629718e50318f7d7fe6723651b4773068c796293543f4ca8ce904688154902ef6d33e7d398e5671c30bd353d11ed2decc651f0f8f0bb3e0f74caa55513965fbf3a1b4139148ef21820be2446fbb6f1061fa7a4099209cef7f88f8feab8bbf4eb0da7498df46566b466db240e64bad1f2608e13c1f3a7104a5e11fcab0a')

functions = Functions(client)

execution = functions.create_execution(
    function_id='6694e3f20038dbbfd7d8',
    path='@appwrite.io',
    method=ExecutionMethod.GET,
    headers={
        'x-action': 'plainTextResponse'
    }
)

print(execution)
