import socket
from clickhouse_driver.client import Client
from Parser import parse_tagged_data

sock = socket.socket()
PORT = 2003
sock.bind(("", PORT))
Taglist = []

if __name__ == "__main__":

    # connection to clickhouse
    client = Client('clickhouse')

    for i in range(100):

        sock.listen(1)
        conn, addr = sock.accept()
        data = conn.recv(512)

        insert_data, Tag_to_add, tags = parse_tagged_data(data)

        if Tag_to_add != [] and Tag_to_add != None:
            for tag in Tag_to_add:
                Taglist.append(tag)
                (client.execute('ALTER TABLE events.tmp ADD COLUMN IF NOT EXISTS ' + tag + ' UInt32 AFTER path'))

        if insert_data != None:
            (client.execute('INSERT INTO events.tmp (' + tags + ') VALUES', [insert_data]))

    print(client.execute('SELECT * FROM events.tmp'))
