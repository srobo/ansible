# [`clatd`](https://github.com/toreanderson/clatd)

A CLAT / SIIT-DC Edge Relay implementation for Linux.

Used to provide IPv4 outbound connectivity to an IPv6-only VM.

It's likely `clat-v6-addr` will need to be configured to assign the correct IP to the created `clat` interface. This may require an additional IPv6 address be routed to the VM. This is configured with the `clatd_conf` variable.
