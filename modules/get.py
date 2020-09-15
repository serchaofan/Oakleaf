import configparser
import re
import os
import pandas as pd


def get_confparser():
    confparser = configparser.ConfigParser()
    root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    hosts_path = f"{root_path}/hosts"
    if not os.path.exists(hosts_path):
        print("hosts file doesn't exists, make sure hosts is well configed")
        exit(0)
    else:
        try:
            confparser.read(hosts_path)
        except Exception as e:
            print(e)
            exit(0)
    return confparser


def get_groups():
    confparser = get_confparser()
    groups = confparser.sections()
    return groups


def get_pass(group, host):
    confparser = get_confparser()
    password = confparser.get(group, host)
    return password


def get_hosts(group):
    confparser = get_confparser()
    hosts = confparser.options(group)
    for host in hosts:
        group_name = group
        hostip = re.match('(.*)@(.*)', host).group(2)
        try:
            hostip_port = re.match('(.*)#(.*)', hostip)
            if hostip_port:
                hostip = hostip_port.group(1)
                sshport = hostip_port.group(2)
            else:
                sshport = 22
        except Exception as e:
            print(e)

        user = re.match('(.*)@(.*)', host).group(1)
        password = get_pass(group, host)
        index = hosts.index(host)
        hosts[index] = dict(hostip=hostip, group=group_name,
                            user=user, password=password, sshport=sshport)
    return hosts


def all_hosts_set():
    hosts = []
    for group in get_groups():
        for host in get_hosts(group):
            hosts.append(host)
    df = pd.DataFrame(hosts)
    df = df.drop_duplicates('hostip')
    hosts = df.to_dict(orient='records')
    return hosts


def print_hosts(args):
    TOPICBAR_HOSTS = "GROUP\tHOSTIP\t\tSSHPORT\tUSER\t\tPASSWORD"
    groups = get_groups()
    if not args.group:
        print(TOPICBAR_HOSTS)
        for group in groups:
            hosts = get_hosts(group)
            for host in hosts:
                group_name = host['group']
                hostip = host['hostip']
                user = host['user']
                password = host['password']
                sshport = host['sshport']
                print(
                    f"{group_name}\t{hostip}\t{sshport}\t{user}\t\t{password}")
    else:
        if args.group not in groups:
            print(f"No Group {args.group}")
        else:
            print(TOPICBAR_HOSTS)
            hosts = get_hosts(args.group)
            for host in hosts:
                group_name = host['group']
                hostip = host['hostip']
                user = host['user']
                password = host['password']
                sshport = host['sshport']
                print(
                    f"{group_name}\t{hostip}\t{sshport}\t{user}\t\t{password}")


def print_groups(args):
    groups = get_groups()
    if not args.group:
        print("GROUP\t\tHOSTS")
        for group in groups:
            group_name = group
            hosts = len(get_hosts(group))
            print(f"{group_name}\t\t{hosts}")
    else:
        if args.group not in groups:
            print(f"No Group {args.group}")
        else:
            print("GROUP\t\tHOSTS")
            group = args.group
            hosts = len(get_hosts(group))
            print(
                f"{args.group}\t\t{hosts}")
