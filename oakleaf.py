from modules.cli import GetCLI, RunCLI, CLI
import sys

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        if sys.argv[1] == 'get':
            GetCLI()
        elif sys.argv[1] == 'run':
            RunCLI()
        elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
            CLI().print_help()
        else:
            print("\033[1;31mWrong Arguments\033[0m")
            CLI().print_help()
    elif len(sys.argv) < 2:
        CLI().print_help()
        exit(0)
