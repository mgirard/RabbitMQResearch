#!/usr/bin/env python
import sys
import pika

#connect to server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#open queue and publish message
channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='', routing_key='task_queue', body=message, properties=pika.BasicProperties(delivery_mode=2))
print " [x] Sent %r" % (message,)

connection.close()

