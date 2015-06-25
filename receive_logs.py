#!/usr/bin/env python
import pika
import time

#connect to server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs', type='fanout')

#create  a random uniqueue message queue and bind to the logs exchange
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print '___Waiting for logs. Exit with CTRL+C'

def callback(ch, method, properties, body):
    print " [] Received %r" % (body,)

channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()

