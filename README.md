# Student Robotics' Ansible

[![CI](https://github.com/RealOrangeOne/srobo-server-web/actions/workflows/ci.yml/badge.svg)](https://github.com/RealOrangeOne/srobo-server-web/actions/workflows/ci.yml)

This is the Ansible config for our servers.

## Dependencies

- [vagrant](https://www.vagrantup.com/)
- `./scripts/setup.sh`

## Local development

Local testing is done using vagrant, which fully provisions a VM locally. Ansible is hooked directly into vagrant, such that a regular provision will run the playbooks.

## Deployment

TBC
