from pyrabbit.api import Client

client = Client('localhost:15672', 'guest', 'guest')
client.get_messages('/', 'queue1')
