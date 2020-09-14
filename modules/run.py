import re
import os
from modules.get import get_groups, get_hosts, get_pass, all_hosts_set
from fabric import Connection
from modules.utils import connect


def executor(args, command, hide=True):
    if args.all:
        hosts = all_hosts_set()
        for host in hosts:
            print(f"[{host['hostip']} >> {command}]")
            connect.runner(host=host, command=command, hide=hide)

    else:
        hosts = get_hosts(args.group)
        for host in hosts:
            print(f"[{host['hostip']} >> {command}]")
            connect.runner(host=host, command=command, hide=hide)


def run_ping(args):
    executor(args, 'uname -s')


def run_command(args):
    command = ' '.join(args.command)
    executor(args, command, hide=False)


def run_script(args):
    pass


def run_file(args):
    pass


def run_copy(args):
    pass


def run_sysinfo(args):
    pass


def run_loadinfo(args):
    pass
