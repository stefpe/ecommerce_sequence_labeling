#!/usr/bin/env bash

docker build -t python .
docker run --rm -it -v $PWD:/usr/src/app python $@