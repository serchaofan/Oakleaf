from fabric import Connection
import traceback
from modules.utils.callback import CallBack


def connect_host(host):
    hostip = host['hostip']
    user = host['user']
    password = host['password']
    sshport = host['sshport']
    try:
        conn = Connection(host=hostip, user=user, port=sshport,
                          connect_kwargs={"password": password, 'timeout': 1})
    except Exception as e:
        traceback.format_exc()
        exit(0)
    return conn


def runner(host, command, hide=True):
    conn = connect_host(host)
    callback = CallBack()
    try:
        conn.run('uname -s', hide=True)
        if conn.is_connected:
            try:
                result = conn.run(command, hide=True)
                if result:
                    callback.runner_on_ok(result, hide)
            except Exception as e:
                # traceback.format_exc()
                callback.runner_on_failed(conn, e)
            except KeyboardInterrupt:
                print("Ctrl-C")
                exit(0)
    except Exception as e:
        callback.runner_on_unreachable(conn, e)
        # traceback.format_exc()
