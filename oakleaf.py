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
    subparser_run_command = subparsers_run.add_parser(
        "command", help="Run Command on Hosts")
    subparser_run_command.add_argument("-g", "--group")
    subparser_run_command.add_argument("-a", "--all", action="store_true")
    subparser_run_command.add_argument("-H", "--host")
    subparser_run_command.add_argument("command")
    subparser_run_command.set_defaults(func=run.run_command)

    # run script
    subparser_run_script = subparsers_run.add_parser(
        "script", help="Run Script on Hosts")
    subparser_run_script.add_argument("-g", "--group")
    subparser_run_script.add_argument("-H", "--host")
    subparser_run_script.add_argument("-a", "--all", action="store_true")
    subparser_run_script.add_argument("-f", "--file", required=True)
    subparser_run_command.set_defaults(func=run.run_script)

    # run copy
    subparser_run_copy = subparsers_run.add_parser(
        "copy", help="Copy Files to Hosts")
    subparser_run_copy.add_argument("-g", "--group")
    subparser_run_copy.add_argument("-H", "--host")
    subparser_run_copy.add_argument("-a", "--all", action="store_true")
    subparser_run_copy.add_argument("-f", "--file", required=True)
    subparser_run_copy.add_argument("-o", "--owner")
    subparser_run_copy.add_argument("-p", "--perm")
    subparser_run_command.set_defaults(func=run.run_copy)

    # run file
    subparser_run_file = subparsers_run.add_parser(
        "file", help="Set File's Properties on Hosts")
    subparser_run_file.add_argument("-g", "--group")
    subparser_run_file.add_argument("-H", "--host")
    subparser_run_file.add_argument("-a", "--all", action="store_true")
    subparser_run_file.add_argument("-f", "--file", required=True)
    subparser_run_file.add_argument("-o", "--owner")
    subparser_run_file.add_argument("-p", "--perm")
    subparser_run_command.set_defaults(func=run.run_file)

    # run sysinfo
    subparser_run_sysinfo = subparsers_run.add_parser(
        "sysinfo", help="Get System Info from Hosts")
    subparser_run_sysinfo.add_argument("-g", "--group")
    subparser_run_sysinfo.add_argument("-H", "--host")
    subparser_run_sysinfo.add_argument("-a", "--all", action="store_true")
    subparser_run_command.set_defaults(func=run.run_sysinfo)

    # run loadinfo
    subparser_run_loadinfo = subparsers_run.add_parser(
        "loadinfo", help="Get System Load Info from Hosts")
    subparser_run_loadinfo.add_argument("-g", "--group")
    subparser_run_loadinfo.add_argument("-H", "--host")
    subparser_run_loadinfo.add_argument("-a", "--all", action="store_true")
    subparser_run_command.set_defaults(func=run.run_loadinfo)

    args = parser.parse_args()
    args.func(args)
