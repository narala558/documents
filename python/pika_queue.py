import time
import random

import pika


url = 'amqp://guest:guest@localhost:5672/%2F'
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)

channel = connection.channel()


queues = ['queue1', 'queue2']
messages = ['foo', 'bar']


while True:
    queue = random.choice(queues)
    message = random.choice(messages)

    channel.queue_declare(queue=queue)
    channel.basic_publish(
        exchange=queue, routing_key=queue, body=message,
        properties=pika.BasicProperties(
            delivery_mode = 2, # make message persistent
        )
    )
    print("{}:{}".format(queue, message))
    time.sleep(1)


connection.close()
