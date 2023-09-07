#!/bin/bash
[[ $# -lt 1 ]] && echo "Usage: $0 <mosquitto_cmd> <args>" && exit 1
cmd=$1
shift
docker exec $(docker container ls | grep eclipse-mosquitto | cut -d " " -f1) /usr/bin/mosquitto_${cmd} "$@"
