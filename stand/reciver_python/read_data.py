import socket
from clickhouse_driver.client import Client
import time

from reciver_python.Parser import parse_tagged_data

sock = socket.socket()
PORT = 2003
sock.bind(("", PORT))
Taglist = []

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

    for i in range(10):

        sock.listen(1)
        conn, addr = sock.accept()
        data = conn.recv(100)
        udata = data.decode("utf-8")
        data = udata.split()
        print("Data: ", data)

        insert_data, Tag_to_add, tags = parse_tagged_data(data)

        if Tag_to_add != []:
            for tag in Tag_to_add:
                Taglist.append(tag)
                print(client.execute('ALTER TABLE events.tmp ADD COLUMN IF NOT EXISTS' + tag + 'UInt32 AFTER last_volume'))

            print(client.execute('INSERT INTO events.tmp (' + tags + ') VALUES', insert_data))

        print(client.execute('SELECT * FROM events.tmp'))






















