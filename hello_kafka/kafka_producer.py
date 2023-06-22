from confluent_kafka import Producer
import socket

conf = {
    'bootstrap.servers': "localhost:9092",
    'client.id': socket.gethostname()
}


producer = Producer(conf)


def acked(err, msg):
    print("Hello")
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))


producer.produce("mapsaCamp", partition=1, key="camp",
                 value="Hello !!", callback=acked)
producer.poll(2)
