# Competitor Services Reverse Proxy

This ansible role fronts a deployment of the competitor services machine's web
services. Currently this is just the [Code Submitter](../code-submitter/README.md).

## Getting Started

1. Follow the [general instructions](../../README.md) for ansible development.

2. Visit <https://sr-competitorsvcs> in a browser (approve the self-signed local TLS
   certificate if needed), and confirm that you see a copy of the SR website
   (also check that you didn't get redirect to the real one!)

3. Make your changes to [`templates/nginx.conf`](templates/nginx.conf)

4. Reprovision the VM, thus deploying the changes: `vagrant provision sr-competitorsvcs`

5. Refresh your browser and bask in the glory of your changes

## Making changes

When you've made a change, either push it to a forked repository, or to a
feature branch, and [raise a pull request][raise-a-pr].

[raise-a-pr]: https://github.com/srobo/ansible/pull/new
