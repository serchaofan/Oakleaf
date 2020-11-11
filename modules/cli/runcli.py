import argparse
from modules import get, run


def parser_ping_options(parser):
    parser.add_argument(
        "-g", "--group", help="Ping Hosts in Group")
    parser.add_argument("-H", "--host", help="Ping Single Host")
    parser.add_argument(
        "-A", "--all", action="store_true", help="Ping All Hosts")
    parser.set_defaults(func=run.run_ping)


def parser_command_options(parser):
    parser.add_argument("-g", "--group")
    parser.add_argument("-A", "--all", action="store_true")
    parser.add_argument("-H", "--host")
    parser.add_argument("command", nargs=argparse.REMAINDER)
    parser.set_defaults(func=run.run_command)


def parser_script_options(parser):
    parser.add_argument("-g", "--group")
    parser.add_argument("-H", "--host")
    parser.add_argument("-A", "--all", action="store_true")
    parser.add_argument("-f", "--file", required=True)
    parser.add_argument("-a", "--argv", nargs=argparse.REMAINDER)
    parser.set_defaults(func=run.run_script)


def parser_copy_options(parser):
    parser.add_argument("-g", "--group")
    parser.add_argument("-H", "--host")
    parser.add_argument("-A", "--all", action="store_true")
    parser.add_argument("-f", "--file", required=True)
    parser.add_argument("-d", "--dest")
    parser.add_argument("-o", "--owner")
    parser.add_argument("-p", "--perm")
    parser.set_defaults(func=run.run_copy)


def parser_file_options(parser):
    parser.add_argument("-g", "--group")
    parser.add_argument("-H", "--host")
    parser.add_argument("-A", "--all", action="store_true")
    parser.add_argument("-r", action="store_true")
    parser.add_argument("-f", "--file", required=True)
    parser.add_argument("-o", "--owner")
    parser.add_argument("-p", "--perm")
    parser.set_defaults(func=run.run_file)


def parser_sysinfo_options(parser):
    parser.add_argument("-g", "--group")
    parser.add_argument("-H", "--host")
    parser.add_argument("-A", "--all", action="store_true")
    parser.set_defaults(func=run.run_sysinfo)


def parser_loadinfo_options(parser):
    parser.add_argument("-g", "--group")
    parser.add_argument("-H", "--host")
    parser.add_argument("-A", "--all", action="store_true")
    parser.set_defaults(func=run.run_loadinfo)


def parser_chpass_options(parser):
    parser.add_argument("-g", "--group")
    parser.add_argument("-H", "--host")
    parser.add_argument("-u", "--user", required=True)
    parser.add_argument("-p", "--passwd", required=True)
    parser.set_defaults(func=run.run_chpass)


def parser_download_options(parser):
    parser.add_argument("-g", "--group")
    parser.add_argument("-H", "--host")
    parser.add_argument("-A", "--all", action="store_true")
    parser.add_argument("--url", required=True)
    parser.set_defaults(func=run.run_download)