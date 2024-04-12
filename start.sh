#!/bin/bash

if [ $(which docker-compose) ]; then
  DOCKER_COMPOSE=docker-compose
elif [ $(which docker compose) ]; then 
  DOCKER_COMPOSE="docker compose"
else
  echo ## CANNOT FIND DOCKER COMPOSE
  exit 1
fi

${DOCKER_COMPOSE} -f docker-compose.yml up -d
