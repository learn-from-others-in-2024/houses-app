import pika
import json
import os

# Input your rabbitmq url
params = pika.URLParameters(os.getenv("RABBIT_AMQP_URL"))

# Create a connection
connection = pika.BlockingConnection(params)

channel = connection.channel()


# Create a publisher
def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='config',
                          body=json.dumps(body), properties=properties)
