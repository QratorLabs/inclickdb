#!/bin/sh

key=$(<../demo2/grafana-key/key.txt)
req='/d-solo/JE7rYbjmz/dh?orgId=1&panelId=2&width=1000&height=500'
curl 'http://localhost:3000/render'$req \
-H 'Authorization: Bearer '$key \
--compressed > ./snapshots/output.png
