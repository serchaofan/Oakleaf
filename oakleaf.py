from fabric import Connection
import argparse
from modules import get, run


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="oakleaf", description="Oakleaf")
    subparsers = parser.add_subparsers(
        title="Oakleaf Sub Command", metavar="")

    # get
    subparser_get = subparsers.add_parser("get", help="Get Infomation")
    subparsers_get = subparser_get.add_subparsers(metavar="")
    # get hosts
    subparser_get_hosts = subparsers_get.add_parser(
        "hosts", help="Get Hosts Info", aliases=['ho'])
    subparser_get_hosts.add_argument(
        "-g", "--group", help="Get Hosts from Group")
    subparser_get_hosts.set_defaults(func=get.print_hosts)
    # get groups
    subparser_get_groups = subparsers_get.add_parser(
        "groups", help="Get Groups Info", aliases=['gro'])
    subparser_get_groups.add_argument(
        "-g", "--group", help="Get Group Info")
    subparser_get_groups.set_defaults(func=get.print_groups)

    # run
    subparser_run = subparsers.add_parser(
        "run", help="Execute Scripts and Commands on target servers")
    subparsers_run = subparser_run.add_subparsers(metavar="")
    # run ping
    subparser_run_ping = subparsers_run.add_parser("ping", help="Ping hosts")
    subparser_run_ping.add_argument(
        "-g", "--group", help="Ping Hosts in Group")
    subparser_run_ping.add_argument("-H", "--host", help="Ping Single Host")
    subparser_run_ping.add_argument(
        "-a", "--all", action="store_true", help="Ping All Hosts")
    subparser_run_ping.set_defaults(func=run.run_ping)
    # run command

    # run script

    # run copy

    # run file

    args = parser.parse_args()
    args.func(args)
