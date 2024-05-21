import pika
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Input your rabbitmq url
params = pika.URLParameters(os.getenv("RABBIT_AMQP_URL"))


# Create a publisher
def publish(method, body):
    print('Publishing to -> Config Service')

    # Create a connection
    connection = pika.BlockingConnection(params)

    # Create a channel
    channel = connection.channel()

    # Set properties
    properties = pika.BasicProperties(method)
    print('Config Service -> publish() :: Properties: ',
          properties, ' Body: ', body)

    # Publish message
    channel.basic_publish(exchange='', routing_key='config',
                          body=json.dumps(body), properties=properties)

    # Close the channel and connection
    channel.close()
    connection.close()
