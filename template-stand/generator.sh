#!/usr/bin/env bash

SERVER=localhost
PORT=2003
while true; do
	R=$((RANDOM % 100))
	echo "generated.important_metric.0" $R `date +%s` | nc ${SERVER} ${PORT} -w 1
	R1=$((RANDOM % 100 + 50))
	echo "generated.important_metric.1" $R1 `date +%s` | nc ${SERVER} ${PORT} -w 1
done
