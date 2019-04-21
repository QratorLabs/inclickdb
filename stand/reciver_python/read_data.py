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

    # connection to clickhouse%
    client = Client('clickhouse')

    # creating database and table
    print(client.execute("CREATE DATABASE IF NOT EXISTS events"))
    print(client.execute(
        'CREATE TABLE IF NOT EXISTS events.tmp(\n \
            timestmp UInt32, \n \
            path String, \n \
            last_volume UInt32 \n \
        ) ENGINE MergeTree() PARTITION BY timestmp ORDER BY timestmp SETTINGS index_granularity=8192;'))

    print(client.execute('SELECT * FROM events.tmp'))

    for i in range(100):
        sock.listen(1)
        conn, addr = sock.accept()
        data = conn.recv(100)

        udata = data.decode("utf-8")
        data = udata.split()
        print("Data: ",  data)
        if len(data) == 3:
            timestamp = int(data[2])
            value = int(data[1])
            tmp = data[0].split(';')
            path = tmp[0]
            for tag_value in tmp[1:]:
                tag, value = parse_tag(tag_value)
            print(client.execute('INSERT INTO events.tmp (timestmp, path, last_volume) VALUES',
                                 [{'timestmp': i, 'path': path, 'last_volume': value}]))

    print(client.execute('SELECT * FROM events.tmp'))
    time.sleep(30)



