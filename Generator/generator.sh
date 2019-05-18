#!/usr/bin/env bash

SERVER=localhost
PORT=2003

dockerize -wait tcp://localhost:${PORT}  -timeout 2m
for (( i=1; i <= 10; i++ )) do
	R=$((RANDOM % 100))
	echo my.awesome.path $R `date +%s` | nc ${SERVER} ${PORT} -w 1
done
