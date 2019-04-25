

def parse_tagged_data(data, Taglist=[]):

    '''
    :param data: string form of mectic
    :param Taglist: list of column in table
    :return:
        insert_data - dict of data to insert into table;
        Tag_to_add -  tags that are not in Taglist;
        tags - tags for insert query
    to_do: add type check
    '''

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
        value = int(tag_value.split('=')[1])

        tags += (', ' + tag)

        insert_data[tag] = value
        if tag not in Taglist:
            Tag_to_add.append(tag)

    return insert_data, Tag_to_add, tags




