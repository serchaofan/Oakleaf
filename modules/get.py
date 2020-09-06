import configparser
import re
import os


def get_confparser():
    confparser = configparser.ConfigParser()
    root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    hosts_path = f"{root_path}/hosts"
    if not os.path.exists(hosts_path):
        print("hosts file doesn't exists, make sure hosts is well configed")
        exit(0)
    else:
        confparser.read(hosts_path)
    return confparser


def get_groups():
    confparser = get_confparser()
    sections = confparser.sections()
    groups = [section for section in sections if re.match('^group', section)]
    return groups


def get_hosts(group):
    confparser = get_confparser()
    hosts = confparser.options(group)
    return hosts


def get_hosts_by_group(group):
    confparser = get_confparser()
    hosts = confparser.items(f'group:{group}')
    return hosts


def get_pass(group, host):
    confparser = get_confparser()
    password = confparser.get(group, host)
    return password


def print_hosts(args):
    groups = get_groups()
    if not args.group:
        print("GROUP\t\tHOSTIP\t\t\tUSER\t\tPASSWORD")
        for group in groups:
            for host in get_hosts(group):
                group_name = re.match('(^group):(.*)', group).group(2)
                hostip = re.match('(.*)@(.*)', host).group(2)
                user = re.match('(.*)@(.*)', host).group(1)
                password = get_pass(group, host)
                print(f"{group_name}\t\t{hostip}\t\t{user}\t\t{password}")
    else:
        if f"group:{args.group}" not in groups:
            print(f"No Group {args.group}")
        else:
            print("GROUP\t\tHOSTIP\t\t\tUSER\t\tPASSWORD")
            hosts = get_hosts_by_group(args.group)
            for host in hosts:
                group = args.group
                hostip = re.match('(.*)@(.*)', host[0]).group(2)
                user = re.match('(.*)@(.*)', host[0]).group(1)
                password = host[1]
                print(
                    f"{group}\t\t{hostip}\t\t{user}\t\t{password}")


def print_groups(args):
    groups = get_groups()
    if not args.group:
        print("GROUP\t\tHOSTS")
        for group in groups:
            group_name = re.match('(^group):(.*)', group).group(2)
            hosts = len(get_hosts(group))
            print(
                f"{group_name}\t\t{hosts}")
    else:
        if f"group:{args.group}" not in groups:
            print(f"No Group {args.group}")
        else:
            print("GROUP\t\tHOSTS")
            group = f"group:{args.group}"
            hosts = len(get_hosts(group))
            print(
                f"{args.group}\t\t{hosts}")
