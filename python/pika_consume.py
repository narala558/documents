import pika


def on_message(channel, method_frame, header_frame, body):
    print(method_frame.delivery_tag)
    print(body)
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)


url = 'amqp://guest:guest@localhost:5672/%2F'
params = pika.URLParameters(url)

connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.basic_consume(
    consumer_callback=on_message, queue='queue1'
)
channel.basic_consume(on_message, 'queue2')


try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
connection.close()
