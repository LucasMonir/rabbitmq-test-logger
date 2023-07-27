import pika
import random;
import sys

def create_connection():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    
    return connection;

def create_channel(connection):
    channel = connection.channel()
    channel.exchange_declare(exchange='logger', exchange_type='direct')
    return channel;

def get_rand_message():
    messages = ['the world is ending!', 'dollar prices lowered!!', 'lack of creativiy to create a message'];
    types = ['warning', 'error', 'info']
    return [random.choice(types), random.choice(messages)];

def main():
    connection = create_connection();
    channel = create_channel(connection);
    type, message = get_rand_message();
    
    channel.basic_publish(
    exchange='logger', routing_key=type, body=message)
    print(f" [x] Sent: Type:{type}, Message: {message}")
    connection.close()

main();