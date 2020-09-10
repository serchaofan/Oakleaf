from fabric import Connection
import traceback
from modules.utils.callback import CallBack


def connect_host(host):
    hostip = host['hostip']
    user = host['user']
    password = host['password']
    try:
        conn = Connection(host=hostip, user=user,
                          connect_kwargs={"password": password, 'timeout': 2})
    except Exception as e:
        traceback.format_exc()
        exit(0)
    return conn


def runner(host, command):
    conn = connect_host(host)
    callback = CallBack()
    # print(conn.is_connected)
    # if not conn.is_connected:
    #     callback.runner_on_unreachable(conn.host)
    # else:
    try:
        if conn.run(command, hide=True):
            callback.runner_on_ok(conn)
    except Exception as e:
        traceback.format_exc()
        callback.runner_on_failed(conn, e)
    except KeyboardInterrupt:
        print("Ctrl-C")
        exit(0)
