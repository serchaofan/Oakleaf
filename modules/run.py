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
                       connect_kwargs={"password": password, 'timeout': 2})
        try:
            if c.run('uname -s', hide=True):
                print(f"[+] {hostip} SSH Connected Successfully!")
        except Exception:
            print(f"[-] {hostip} SSH Connection Failed!")
        except KeyboardInterrupt:
            print("Ctrl-C")
            exit(0)
    if args.all:
        hosts = all_hosts_set()
        for host in hosts:
            try:
                run_start_ping(host)
            except Exception as e:
                print(f"Check hosts file, There're Something Wrong with {e}")
    else:
        hosts = get_hosts(args.group)
        for host in hosts:
            try:
                run_start_ping(host)
            except Exception as e:
                print(f"Check hosts file, There're Something Wrong with {e}")


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
