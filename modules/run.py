import re
import os
from .get import get_groups, get_hosts, get_hosts_by_group, get_pass
from fabric import Connection


def run_ping(args):
    print(args)
