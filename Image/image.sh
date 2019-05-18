#!/bin/sh


key=$(cat grafana-key/key.txt)
curl 'http://stand_grafana_1:3000/render/d-solo/JE7rYbjmz/dh?orgId=1&panelId=2&width=1000&height=500&tz=Europe%2FMoscow' -H 'Authorization: Bearer '$key --compressed > ./snapshots/output.png
sleep 20
