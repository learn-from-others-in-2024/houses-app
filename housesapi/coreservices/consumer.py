import pika
import json
import os
from dotenv import load_dotenv
from core import create_app, db, House

# Load environment variables from .env file
load_dotenv()

params = pika.URLParameters(os.getenv("RABBIT_AMQP_URL"))
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='core')

# Create the Flask application
app = create_app()


def callback(ch, method, properties, body):
    data = json.loads(body)
    print(data)
    print('Received in core', data, ' Properties: ', properties)

    with app.app_context():
        if properties.content_type == 'house_created':
            house = House(id=data['id'], name=data['name'],
                          image=data['image'], description=data['description'])
            db.session.add(house)
            db.session.commit()
            print('House Created')

        elif properties.content_type == 'house_updated':
            house = House.query.get(data['id'])
            if house:
                house.name = data['name']
                house.image = data['image']
                house.description = data['description']
                db.session.commit()
                print('House Updated')

        elif properties.content_type == 'house_deleted':
            house = House.query.get(data)
            if house:
                db.session.delete(house)
                db.session.commit()
                print('House Deleted')


channel.basic_consume(
    queue='core', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
