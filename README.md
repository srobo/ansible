# Student Robotics' Ansible

[![CI](https://github.com/RealOrangeOne/srobo-server-web/actions/workflows/ci.yml/badge.svg)](https://github.com/RealOrangeOne/srobo-server-web/actions/workflows/ci.yml)

This is the Ansible config for our servers.

## Dependencies

- [VirtualBox](https://www.virtualbox.org/) (or another virtual machine tool)
- [vagrant](https://www.vagrantup.com/)
- `./scripts/setup.sh`

## Local development

Local testing is done using vagrant, which fully provisions a VM locally. Ansible is hooked directly into vagrant, such that a regular provision will run the playbooks.

### Getting started

Spin up the VMs with:

```
vagrant up
```

On first run this will download the base OS images as needed, create the VMs in
Virtualbox and then also provision them -- applying the ansible configuration.
As a result this can take a few minutes.

Specifying the name of one of the machines (e.g: `vagrant up sr-proxy`) will
do this for just that machine.

If you need to apply the ansible config again you can do this with:

```
vagrant provision
```

### Accessing the VMs

Should you need **SSH** access to the machines you can do this via `vagrant ssh`.
This will log you in as the `vagrant` user, which has passwordless sudo.

You may wish to configure a hosts entry for easily accessing the VM, for example
to test any **HTTP** services they're running. Add the following line to
`/etc/hosts` on the *host* machine:

```
192.168.56.56  sr-proxy sr-proxy.local
192.168.56.57  sr-compsvc sr-compsvc.local
```

You'll then be able to access the machines as if they were hosted. For example
visiting <https://sr-proxy> in your browser will serve you the SR homepage
(though your browser may complain, correctly, about the TLS certificate not
being signed).

### More details

Mapping of these development VMs into Ansible's playbooks is handled via the `Vagrantfile`, see e.g: the `ansible.groups` mapping, from which vagrant will build the appropriate ansible inventory. This therefore needs to be manually kept in a state which reflects the production inventory defined by the `hosts` file.

See <https://developer.hashicorp.com/vagrant/docs/provisioning/ansible> for more details on how Vagrant's Ansible provisioner works.

## Deployment

Deployment is currently manual. Once changes are approved someone with access to
the target machines (currently members of the Infrastructure Team Committee,
though others could be added via this repo) will apply the changes manually.

To aid with this there is a script at `scripts/apply`. This should be run first
with `--check --diff` to validate the changes and then without `--check` in
order to apply them.
