#!/usr/bin/env bash
SERVER=localhost
PORT=2003
while true; do
	R=$((RANDOM % 100))
	echo "my.awesome.path1;boo=123;a=1" $R `date +%s` | nc ${SERVER} ${PORT} -w 1
	echo "my.awesome.path1;boo=123;a=1;tyty="$R*2 $R `date +%s` | nc ${SERVER} ${PORT} -w 1
done
