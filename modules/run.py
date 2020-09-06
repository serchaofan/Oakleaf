import re
import os
from .get import get_groups, get_hosts, get_pass, all_hosts_set
from fabric import Connection


def run_ping(args):
    def run_start_ping(host):
        hostip = host['hostip']
        user = host['user']
        password = host['password']
        c = Connection(host=hostip, user=user,
                       connect_kwargs={"password": password})
        if c.is_connected:
            print(f"[+] {hostip} SSH Connected Successfully!")
        else:
            print(f"[-] {hostip} SSH Connected Failed!")
    print(args)
    groups = get_groups()
    hosts = []
    if args.all:
        hosts = all_hosts_set()
        print(hosts)
        for host in hosts:
            run_start_ping(host)
    else:
        hosts = get_hosts(args.group)
        for host in hosts:
            run_start_ping(host)
