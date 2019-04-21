import socket
from clickhouse_driver.client import Client
import time

sock = socket.socket()
PORT = 2003
sock.bind(("", PORT))
taglist = []

def parse_tag(tag_value):
    tag = tag_value.split('=')[0]
    value = float(tag_value.split('=')[1])
    if tag not in taglist:
        taglist.append(tag)
    return tag, value


if __name__ == "__main__":

    client = Client('clickhouse')
    print('aaaaaaaaaaaaaaaaa')
    print(client.execute("CREATE DATABASE IF NOT EXISTS events"))
    print(client.execute(
        'CREATE TABLE IF NOT EXISTS events.tmp(\n \
            timestmp UInt32, \n \
            path String, \n \
            last_volume UInt32 \n \
        ) ENGINE MergeTree() PARTITION BY timestmp ORDER BY timestmp SETTINGS index_granularity=8192;'))

    print(client.execute('SELECT * FROM events.tmp'))

    print(client.execute('INSERT INTO events.tmp (timestmp, path, last_volume) VALUES',
                         [{'timestmp': 1, 'path': "uuytyt", 'last_volume': 31}]))
    print(client.execute('SELECT * FROM events.tmp'))
    print('aaaaaaaaaaaaaaaaaaaaaa')
    time.sleep(30)



