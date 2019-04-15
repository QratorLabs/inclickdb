import socket

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

    #for i in range(100):
    while True:
        sock.listen(1)
        conn, addr = sock.accept()
        data = conn.recv(100)

        udata = data.decode("utf-8")
        data = udata.split()
        timestamp = data[-1]
        value = data[-2]
        tmp = data[-3].split(';')
        path = tmp[0]
        for tag_value in tmp[1:]:
            tag, value = parse_tag(tag_value)

        print("Data: " + udata)
