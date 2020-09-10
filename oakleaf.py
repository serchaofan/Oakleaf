from modules.cli import GetCLI, RunCLI
import sys

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        if sys.argv[1] == 'get':
            GetCLI()
        elif sys.argv[1] == 'run':
            RunCLI()
    else:
        print("usage: oakleaf get|run ...")
        exit(0)
