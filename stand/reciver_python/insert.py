from clickhouse_driver.client import Client

client = Client('clickhouse')

print(client.execute('INSERT INTO tmp \n\
                        (path, last_volume) VALUES\n\
                        ( \"tytyt\", 31)'))