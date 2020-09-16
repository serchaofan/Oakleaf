import re
import os
from modules.get import get_groups, get_hosts, get_pass, all_hosts_set
from fabric import Connection
from modules.utils import connect


def executor(args, command, hide=True):
    if args.all:
        hosts = all_hosts_set()
        for host in hosts:
            print(
                f"[\033[1;32m{host['hostip']}\033[0m >> \033[7;32m{command}\033[0m]")
            connect.runner(host=host, command=command, hide=hide)

    else:
        hosts = get_hosts(args.group)
        for host in hosts:
            print(
                f"[\033[1;32m{host['hostip']}\033[0m >> \033[7;32m{command}\033[0m]")
            connect.runner(host=host, command=command, hide=hide)


def transferor(args):
    if args.all:
        hosts = all_hosts_set()
        for host in hosts:
            print(
                f"[\033[1;32m{host['hostip']}\033[0m >> \033[7;32m{args.file}\033[0m]")
            if args.dest:
                connect.transfer(host=host, file=args.file, remote=args.dest)
            else:
                connect.transfer(host=host, file=args.file)

    else:
        hosts = get_hosts(args.group)
        for host in hosts:
            print(
                f"[\033[1,32m{host['hostip']}\033[0m >> \033[7;32m{args.file}\033[0m]")
            if args.dest:
                connect.transfer(host=host, file=args.file, remote=args.dest)
            else:
                connect.transfer(host=host, file=args.file)


def run_ping(args):
    executor(args, 'uname -s')


def run_command(args):
    command = ' '.join(args.command)
    executor(args, command, hide=False)


def run_script(args):
    args.dest = "/tmp"
    args.owner = 'root'
    args.perm = '754'
    run_copy(args)
    argv = ''
    if args.argv:
        argv = ' '.join(args.argv)
        if argv[0] == '\'' and argv[-1] == '\'':
            argv = argv.strip('\'')
    filename = os.path.split(args.file)[1]
    command = f"/bin/sh /tmp/{filename} {argv}"
    executor(args, command, hide=False)


def run_file(args):
    if not args.file:
        print("Pls Specify One File on Target Hosts")
        exit(0)
    if not (args.owner or args.perm):
        print("You Must Specify Owner or Perm That You want to Change")
        exit(0)

    if args.owner:
        if args.r:
            command = f"chown {args.owner}:{args.owner} {args.file}"
            executor(args, command)
        else:
            command = f"chown -R {args.owner}:{args.owner} {args.file}"
            executor(args, command)
    if args.perm:
        if re.match('(\d){3,3}', args.perm):
            if args.r:
                command = f"chmod -R {args.perm} {args.file}"
                executor(args, command)
            else:
                command = f"chmod {args.perm} {args.file}"
                executor(args, command)
        else:
            print("Pls Input Right Perm Number")
            exit(0)


def run_copy(args):
    if not args.file:
        print("Pls Specify One File on Target Hosts")
        exit(0)
    if not os.path.exists(args.file):
        print("Not Exists")
        exit(0)
    transferor(args)
    filename = os.path.split(args.file)[1]
    if args.dest:
        if args.dest[-1] == '/':
            args.dest = args.dest.rstrip('/')
        filepath = f"{args.dest}/{filename}"
    else:
        filepath = f"/tmp/{filename}"
    if args.owner:
        command = f"chown -R {args.owner}:{args.owner} {filepath}"
        executor(args, command)
    if args.perm:
        if re.match('(\d){3,3}', args.perm):
            command = f"chmod -R {args.perm} {filepath}"
            executor(args, command)
        else:
            print("Pls Input Right Perm Number")
            exit(0)


def run_sysinfo(args):
    pass


def run_loadinfo(args):
    pass


def run_gitscript(args):
    print(args)
