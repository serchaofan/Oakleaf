import argparse
from modules import get, run
from modules.cli import getcli
from modules.cli import runcli


class CLI():
    def __init__(self, callback=None):
        self.parser = argparse.ArgumentParser(
            prog="oakleaf", description="Oakleaf")
        self.callback = callback
        self.subparsers = self.parser.add_subparsers(
            title="Oakleaf Sub Command", metavar="")

        self.subparser_get = self.subparsers.add_parser(
            "get", help="Get Infomation")
        self.subparsers_get = self.subparser_get.add_subparsers(metavar="")
        self.subparser_run = self.subparsers.add_parser(
            "run", help="Execute Scripts and Commands on target servers")
        self.subparsers_run = self.subparser_run.add_subparsers(metavar="")


class GetCLI(CLI):
    def __init__(self):
        CLI.__init__(self)

        self.parser_hosts = self.subparsers_get.add_parser(
            "hosts", help="Get Hosts Info", aliases=['ho'])
        getcli.parser_hosts_options(self.parser_hosts)

        self.parser_groups = self.subparsers_get.add_parser(
            "groups", help="Get Groups Info", aliases=['gro'])
        getcli.parser_groups_options(self.parser_groups)

        args = self.parser.parse_args()
        args.func(args)


class RunCLI(CLI):
    def __init__(self):
        CLI.__init__(self)

        self.parser_ping = self.subparsers_run.add_parser(
            "ping", help="Ping hosts")
        runcli.parser_ping_options(self.parser_ping)

        self.parser_command = self.subparsers_run.add_parser(
            "command", help="Run Command on Hosts")
        runcli.parser_command_options(self.parser_command)

        self.parser_script = self.subparsers_run.add_parser(
            "script", help="Run Script on Hosts")
        runcli.parser_script_options(self.parser_script)

        self.parser_copy = self.subparsers_run.add_parser(
            "copy", help="Copy Files to Hosts")
        runcli.parser_copy_options(self.parser_copy)

        self.parser_file = self.subparsers_run.add_parser(
            "file", help="Set File's Properties on Hosts")
        runcli.parser_file_options(self.parser_file)

        self.parser_sysinfo = self.subparsers_run.add_parser(
            "sysinfo", help="Get System Info from Hosts")
        runcli.parser_sysinfo_options(self.parser_sysinfo)

        self.parser_loadinfo = self.subparsers_run.add_parser(
            "loadinfo", help="Get System Load Info from Hosts")
        runcli.parser_loadinfo_options(self.parser_loadinfo)
