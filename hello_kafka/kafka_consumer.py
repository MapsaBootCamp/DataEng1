from confluent_kafka import Consumer
from confluent_kafka import KafkaError, KafkaException
import sys

conf = {
    'bootstrap.servers': "localhost:9092",
    'group.id': "camp-2",
    'auto.offset.reset': 'latest'
}

consumer = Consumer(conf)

consumer.subscribe(["mapsaCamp"])

while True:
    msg = consumer.poll()
    if msg is None:
        continue

    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            # End of partition event
            sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                             (msg.topic(), msg.partition(), msg.offset()))
        elif msg.error():
            raise KafkaException(msg.error())
    else:
        key = msg.key().decode("utf-8")
        data = msg.value().decode("utf-8")
        print(key, data)
