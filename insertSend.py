#!/usr/bin/env python
import sys
import pika

#connect to server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#open queue and publish message
channel.queue_declare(queue='hello')

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='', routing_key='hello', body=message)
print " [x] Sent %r" % (message,)

connection.close()

