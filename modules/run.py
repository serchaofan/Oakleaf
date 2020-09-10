import re
import os
from .get import get_groups, get_hosts, get_pass, all_hosts_set
from fabric import Connection
from modules.utils import connect


def run_ping(args):
    if args.all:
        hosts = all_hosts_set()
        for host in hosts:
            connect.runner(host=host, command='uname -s')

    else:
        hosts = get_hosts(args.group)
        for host in hosts:
            connect.runner(host=host, command='uname -s')


def run_command(args):
    pass


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
