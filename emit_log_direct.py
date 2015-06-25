#!/usr/bin/env python
import sys
import pika

#connect to server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#open and create exchange
channel.exchange_declare(exchange='direct_logs', type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'

#publish message to the exchange
message = ' '.join(sys.argv[2:]) or "Hello World!"
channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)
print "-Sent %r:%r" % (severity, message)

connection.close()

