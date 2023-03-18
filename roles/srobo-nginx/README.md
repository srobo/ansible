# Student Robotics Website Reverse Proxy

This ansible role pulls together all the pieces of the Student Robotics public
website.

## Getting Started

1. Follow the [general instructions](../../README.md) for ansible development.

2. Visit <https://sr-proxy> in a browser (approve the self-signed local TLS
   certificate if needed), and confirm that you see a copy of the SR website
   (also check that you didn't get redirect to the real one!)

3. Make your changes to [`templates/nginx.conf`](templates/nginx.conf)

4. Reprovision the VM, thus deploying the changes: `vagrant provision sr-proxy`

5. Refresh your browser and bask in the glory of your changes

## Making changes

When you've made a change, either push it to a forked repository, or to a
feature branch, and [raise a pull request][raise-a-pr].

[raise-a-pr]: https://github.com/srobo/ansible/pull/new
