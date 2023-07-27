import pika
import sys


def create_connection_channel():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel();
    channel.exchange_declare(exchange='logger', exchange_type='direct')
    return channel;

def queue_configuration(channel):
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue
    return queue_name;

def set_queue_type(channel, queue_name):
    types = sys.argv[1:]
    if not types:
        sys.stderr.write("Please, initiate code with a type of log (without '[' and ']'): %s [info] [warning] [error]\n" % sys.argv[0])
        sys.exit(1)

    for type in types:
        channel.queue_bind(
            exchange='logger', queue=queue_name, routing_key=type)

def callback(ch, method, properties, body):
    print(f"[x] {method.routing_key}:{body.decode()}, log mockingly saved!")

def main():
    channel  = create_connection_channel();
    queue = queue_configuration(channel);
    set_queue_type(queue_name=queue, channel=channel)

    channel.basic_consume(
        queue=queue, on_message_callback=callback, auto_ack=True)
    
    print(' [*] Waiting for logs to be consumed...')

    channel.start_consuming()


main()