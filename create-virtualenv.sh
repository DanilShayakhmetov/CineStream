#!/usr/bin/env bash

virtualenv -p python3 ./env
source ./env/bin/activate

pip3 install -r app/requirements.txt