#!/usr/bin/env python
import sys
import pika

#connect to server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#open and create exchange
channel.exchange_declare(exchange='logs', type='fanout')

#publish message to the exchange
message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print " [x] Sent %r" % (message,)

connection.close()

