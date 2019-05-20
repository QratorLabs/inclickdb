#!/usr/bin/env bash

SERVER=localhost
PORT=2003
while true; do
	R=$((RANDOM % 10))
	echo "my.awesome.path1;host=local;id=0;tag1=0" $R `date +%s` | nc ${SERVER} ${PORT} -w 1
	R1=$((RANDOM % 10 + 10))
	echo "my.awesome.path1;host=local;id=1;tag1=0;tag2=0" $R1 `date +%s` | nc ${SERVER} ${PORT} -w 1
	R2=$((RANDOM % 10 + 20))
	echo "my.awesome.path1;host=local;id=2;tag2=0" $R2 `date +%s` | nc ${SERVER} ${PORT} -w 1
done
