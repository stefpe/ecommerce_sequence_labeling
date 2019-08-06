#!/usr/bin/env bash

docker run --rm -it -v $PWD:/usr/src -w /usr/src python:3 pip install --no-cache-dir -r requirements.txt && bash