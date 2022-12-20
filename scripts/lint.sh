#!/usr/bin/env bash

set -e

PATH=${PWD}/env/bin:${PATH}

set -x

yamllint --strict --config-file yamllint.yml $PWD

ansible-lint playbook.yml --parseable --config-file .ansible-lint

ansible-playbook playbook.yml --syntax-check
