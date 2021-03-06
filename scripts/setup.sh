#!/usr/bin/env bash

set -e

PATH=${PWD}/env/bin:${PATH}

set -x

python3 -m venv env

pip install -U pip setuptools wheel

pip install -r dev-requirements.txt

ansible-galaxy install -r galaxy-requirements.yml
