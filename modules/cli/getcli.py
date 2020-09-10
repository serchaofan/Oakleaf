import argparse
from modules import get, run


def parser_hosts_options(parser):
    parser.add_argument("-g", "--group", help="Get Hosts from Group")
    parser.set_defaults(func=get.print_hosts)


def parser_groups_options(parser):
    parser.add_argument("-g", "--group", help="Get Group Info")
    parser.set_defaults(func=get.print_groups)
