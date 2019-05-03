import datetime


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


def is_match(tmp, data, names, Taglist=[]):
    tmp = tmp.split('.')
    data = data.split()
    data_ = data[0].split('.')
    names = names.split('.')
    insert_data = dict()
    path = ''
    last_volume = ''
    Tag_to_add = []
    tags = 'timestmp, path, last_volume'

    for i in range(len(tmp)):
        if tmp[i] != '*':
            if data_[i] != tmp[i]:
                return None, None, None
        if names[i] == 'measurement':
            path += data_[i] + '.'
        elif names[i] == 'field':
            last_volume += data_[i]
        elif names[i] != '':
            insert_data[names[i]] = data_[i]
            if names[i] not in Taglist:
                Tag_to_add.append(names[i])
            tags += (', ' + names[i])

    insert_data[last_volume] = data[-1]
    insert_data['path'] = path
    insert_data['timestmp'] = int(str(datetime.datetime.timestamp(datetime.datetime.now())).split('.')[0])
    return insert_data, Tag_to_add, tags


def parse_tamplate(filename, data, Taglist=[]):
    if type(filename) == str:
        f = open(filename, 'r')
    else:
        f = filename

    for line in f:
        L = line.split()
        insert_data, Tag_to_add, tags = is_match(L[0], data, L[1], Taglist)

        if insert_data:
            return insert_data, Tag_to_add, tags
    return None, None, None

