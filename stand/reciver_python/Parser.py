
def parse_tagged_data(data, Taglist=[]):

    if type(data) != str:
        data = data.decode("utf-8")

    data = data.split()
    if len(data) != 3:
        return None, None, None

    insert_data = dict()
    insert_data['timestmp'] = int(data[2])
    insert_data['last_volume'] = int(data[1])
    data = data[0].split(';')
    insert_data['path'] = data[0]
    Tag_to_add = []
    data = data[1:]
    tags = 'timestmp, path, last_volume'
    for tag_value in data:

        tag = tag_value.split('=')[0]
        value = tag_value.split('=')[1]

        tags += (', ' + tag)

        insert_data[tag] = value
        if tag not in Taglist:
            Tag_to_add.append(tag)

    return insert_data, Tag_to_add, tags




if __name__ == "__main__":
    data = 'my.awesome.path1;b=123;a=1;c=5 71 1555849096'
    ins, T, tags = (parse_tagged_data(data, []))
    if ins!= None :
        print(ins, T)
        print(tags)




