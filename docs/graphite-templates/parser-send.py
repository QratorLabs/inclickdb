import re
import socket
import time
import random

class Template:
    def __init__(self):
        self.filter = None
        self.matcher = None
        self.default = []
        
    def match(self, metric):
        if self.filter is None:
            return True
        return self.filter.match(metric) is not None
    
    def parse(self, metrics, sep, default_tags, value):
        measurement = ''
        field_name = 'value'
        tags = {}
        for tag in default_tags:
            name, val = tag.split('=')
            tags[name] = val
        for tag in self.default:
            name, val = tag.split('=')
            tags[name] = val
        for i in range(len(metrics)):
            name = self.matcher[i]
            val = metrics[i]
            if '' == name:
                continue
            if 'measurement' == name:
                measurement += sep + val
            elif 'measurement*' == name:
                measurement += sep + sep.join(list(metrics[k] for k in range(i, len(metrics))))
                break
            elif 'field' == name:
                field_name = val
            elif 'field*' == name:
                field_name = sep.join(list(metrics[k] for k in range(i, len(metrics))))
                break
            else:
                tags[name] = val
        
        answer = measurement[1:]
        answer += ',' + ','.join(['='.join(k) for k in tags.items()])
        answer += ' ' + field_name + '=' + value
        return answer
    
class MetricParser:
    def __init__(self, sep='.', default_tags=None):
        self.sep = sep
        self.default_tags = default_tags.split(',')
        self.templates = []
        
    def add(self, template):
        tokens = template.split()
        t = Template()
        filter_index = matcher_index = default_index = 3
        if len(tokens) == 3:
            filter_index = 0
            matcher_index = 1
            default_index = -1
        elif len(tokens) == 2:
            if '=' in tokens[-1]:
                matcher_index = 0
                default_index = -1
            else:
                filter_index = 0
                matcher_index = 1
        else:
            matcher_index = 0
        t.matcher = tokens[matcher_index].split('.')
        if filter_index != 3:
            t.filter = re.compile(tokens[filter_index].replace('.', '\.').replace('*', '[^\.]*'))
        if default_index != 3:
            t.default = tokens[default_index].split(',')
        self.templates.append(t)
        return self
    
    def parse(self, metric):
        try:
            metric, value = metric.split(' ')
            for t in self.templates:
                if t.match(metric):
                    return t.parse(metric.split('.'), self.sep, self.default_tags, value)
        except ValueError:
            print("Invalid format")


parser = MetricParser(sep='_', default_tags='region=moscow,answer=42')
parser = parser.add('servers.* .host.resource.measurement.field.measurement* extra_tag=extra_value')\
.add('stats.* .host.name.measurement*')\
.add('failures.*.db1 ...type.measurement.field')\
.add('.measurement*')


import requests

address = 'http://localhost:8086/write?db=graphite'

while True:
    value = random.uniform(-100, 100)
    time.sleep(1)
    data = parser.parse('servers.local.gpu.prefix.avg.middle.suffix {0}').format(value)
    r = requests.post(address, data=data)
