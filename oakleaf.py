from fabric import Connection
import argparse
from modules import get, run
from modules.cli import CLI, GetCLI, RunCLI


if __name__ == '__main__':
    GetCLI()
    RunCLI()
