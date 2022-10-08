# Student Robotics' Ansible

[![CI](https://github.com/RealOrangeOne/srobo-server-web/actions/workflows/ci.yml/badge.svg)](https://github.com/RealOrangeOne/srobo-server-web/actions/workflows/ci.yml)

This is the Ansible config for our servers.

## Dependencies

- [VirtualBox](https://www.virtualbox.org/) (or another virtual machine tool)
- [vagrant](https://www.vagrantup.com/)
- `./scripts/setup.sh`

## Local development

Local testing is done using vagrant, which fully provisions a VM locally. Ansible is hooked directly into vagrant, such that a regular provision will run the playbooks.

You may wish to configure a hosts entry for easily accessing the VM, if so add
the following line to `/etc/hosts` on the *host* machine:

```
192.168.56.56  sr-proxy sr-proxy.local
```

## Deployment

Deployment is currently manual. Once changes are approved someone with access to
the target machines (currently members of the Infrastructure Team Committee,
though others could be added via this repo) will apply the changes manually.

To aid with this there is a script at `scripts/apply`. This should be run first
with `--check --diff` to validate the changes and then without `--check` in
order to apply them.
