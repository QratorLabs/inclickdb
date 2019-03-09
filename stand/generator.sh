#!/usr/bin/env bash

SERVER=localhost
PORT=2003
while true; do
	R=$((RANDOM % 100))
	echo my.awesome.path $R `date +%s` | nc ${SERVER} ${PORT} -w 1
done
