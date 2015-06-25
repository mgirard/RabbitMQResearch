#!/usr/bin/env python
import sys
import pika

#connect to server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#create exchange
channel.exchange_declare(exchange='topic_logs', type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'

#publish message to the exchange
message = ' '.join(sys.argv[2:]) or "Hello World!"
channel.basic_publish(exchange='topic_logs', routing_key=routing_key, body=message)
print "-Sent %r:%r" % (routing_key, message)

connection.close()

