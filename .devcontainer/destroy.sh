#!/usr/bin/env bash

docker-compose -f ./home-assistant.yaml down --rmi local --volumes --remove-orphans
