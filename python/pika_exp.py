import pika

pika_conn_params = pika.ConnectionParameters(
    host='localhost', port=5672,
    credentials=pika.credentials.PlainCredentials('guest', 'guest'),
)
connection = pika.BlockingConnection(pika_conn_params)

channel = connection.channel()

queue = channel.queue_declare(
    queue="celery", durable=True,
    exclusive=False, auto_delete=False
)
print(queue.method.message_count)


# method_frame, header_frame, body = channel.basic_get('celery')
# if method_frame:
#     print('Consuming a message')
#     print(method_frame, header_frame, body)
#     # channel.basic_ack(method_frame.delivery_tag)
# else:
#     print('No message returned')

def foo():
    pass

channel.basic_consume(foo, queue='celery', no_ack=True)
