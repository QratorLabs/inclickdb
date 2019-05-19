"""insert tagged data into table"""
import socket
from clickhouse_driver.client import Client
from parser_for_taged import parse_tagged_data


def main():
    """
    connects to clickhouse and calls parser and inserts data
    :return: nothing
    """

    sock = socket.socket()
    port = 2003
    sock.bind(("", port))

    taglist = []

    # connection to clickhouse
    client = Client("clickhouse")

    for i in range(100):

        sock.listen(1)
        conn, addr = sock.accept()
        data = conn.recv(512)

        insert_data, tag_to_add, tags, taglist = parse_tagged_data(data, taglist)

        if tag_to_add != [] and tag_to_add:
            for tag in tag_to_add:
                taglist.append(tag)
                (
                    client.execute(
                        "ALTER TABLE events.tmp ADD \
                COLUMN IF NOT EXISTS "
                        + tag
                        + " UInt32 AFTER path"
                    )
                )

        if insert_data:
            (
                client.execute(
                    "INSERT INTO events.tmp (" + tags + ") VALUES", [insert_data]
                )
            )

    print(client.execute("SELECT * FROM events.tmp"))


if __name__ == "__main__":
    main()
