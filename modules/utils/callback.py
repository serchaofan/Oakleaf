import logging
import datetime


class CallBack(object):
    def __init__(self):
        self.ok = '[+]'
        self.failed = '[-]'
        self.finish = None
        self.created = datetime.datetime.now()

    def runner_on_ok(self, conn):
        self.finish = datetime.datetime.now()
        spendtime = (self.finish - self.created).microseconds / 1000
        msg = f"{self.ok} {conn.host} Success {int(spendtime)}ms"
        print(msg)

    def runner_on_failed(self, conn, error):
        self.finish = datetime.datetime.now()
        spendtime = (self.finish - self.created).microseconds / 1000
        msg = f"{self.failed} {conn.host} Failed {int(spendtime+1000*conn.connect_kwargs['timeout'])}ms\nReason: {error}"
        print(msg)

    def runner_on_unreachable(self, conn, error):
        self.finish = datetime.datetime.now()
        spendtime = (self.finish - self.created).microseconds / 1000
        msg = f"{self.failed} {conn.host} UnReachable {int(spendtime+1000*conn.connect_kwargs['timeout'])}ms\nReason: {error}"
        print(msg)
