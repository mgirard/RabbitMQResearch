#!/usr/bin/env python
import pika
import sys

#connect to server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='topic_logs', type='topic')

#create  a random uniqueue message queue and bind to the logs exchange
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    print >> sys.stderr, "Usage: %s [binding_key]..." % (sys.argv[0],)
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key=binding_key)

print '...Waiting for logs. Exit with CTRL+C'

def callback(ch, method, properties, body):
    print "++Received %r:%r" % (method.routing_key, body,)

channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()

