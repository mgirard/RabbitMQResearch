#!/usr/bin/env python
import pika

#connect to server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#open queue and publish message
channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. Exit with CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

channel.basic_consume(callback, queue='hello', no_ack=True)

channel.start_consuming()

