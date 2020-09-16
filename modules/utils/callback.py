import datetime


class CallBack(object):
    def __init__(self):
        self.ok = '[+]'
        self.failed = '[-]'
        self.finish = None
        self.created = datetime.datetime.now()

    def runner_on_ok(self, result, hide):
        self.finish = datetime.datetime.now()
        spendtime = (self.finish - self.created).microseconds / 1000
        if hide:
            msg = f"\033[32m{self.ok} {result.connection.host} Success {int(spendtime)}ms\033[0m"
        elif not hide:
            msg = f"\033[32m{self.ok} {result.connection.host} Success {int(spendtime)}ms\nStdout: {result.stdout}\033[0m"
        print(msg)

    def runner_on_failed(self, conn, error):
        self.finish = datetime.datetime.now()
        spendtime = (self.finish - self.created).microseconds / 1000
        msg = f"\033[31m{self.failed} {conn.host} Failed {int(spendtime+1000*conn.connect_kwargs['timeout'])}ms\nReason: {error}\033[0m"
        print(msg)

    def runner_on_unreachable(self, conn, error):
        self.finish = datetime.datetime.now()
        spendtime = (self.finish - self.created).microseconds / 1000
        msg = f"\033[33m{self.failed} {conn.host} UnReachable {int(spendtime+1000*conn.connect_kwargs['timeout'])}ms\nReason: {error}\033[0m"
        print(msg)

    def runner_on_ok_file(self, result):
        self.finish = datetime.datetime.now()
        spendtime = (self.finish - self.created).microseconds / 1000
        msg = f"\033[32m{self.ok} {result.connection.host} Success {int(spendtime)}ms remote: {result.remote}\033[0m"
        print(msg)
