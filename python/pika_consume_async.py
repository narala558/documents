import pika


def callback(ch, method, properties, body):
    print(ch, method, properties, body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_open(connection):
    connection.channel(on_channel_open)


def on_channel_open(channel):
    channel.basic_consume(callback, queue='queue1')
    channel.basic_consume(callback, queue='queue2')


url = 'amqp://guest:guest@localhost:5672/%2F'
parameters = pika.URLParameters(url)
connection = pika.SelectConnection(
    parameters=parameters,
    on_open_callback=on_open
)

try:
    connection.ioloop.start()
except KeyboardInterrupt:
    connection.close()
