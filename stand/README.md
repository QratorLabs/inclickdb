### Store metrics  
#### What is it?

This stand does the following:
- Generates some graphite data
- parses it
- Sends it to [clickhouse]

#### What should I do?

Do the following steps:
- `docker-compose up`
- `bash generator.sh`, `bash generator2.sh` (for generating data)

#### TODO

- Add .sh with cron
- Add grafana