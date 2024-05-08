import pika
import json


# Input your rabbitmq url
params = pika.URLParameters('{{Your_AMQP_URL}}')

# Create a connection
connection = pika.BlockingConnection(params)

channel = connection.channel()


# Create a publisher
def publish(method, body):
    print('Publishing to core')
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='core',
                          body=json.dumps(body), properties=properties)
