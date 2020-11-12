# Oakleaf

<center>

![](./logo.png)

使用 Python Fabric 库编写的简易自动化运维工具，类似 Ansible

![GitHub release (latest by date)](https://img.shields.io/github/v/release/serchaofan/oakleaf)
![GitHub last commit](https://img.shields.io/github/last-commit/serchaofan/oakleaf)
![Travis (.org)](https://img.shields.io/travis/serchaofan/oakleaf)
![Scrutinizer code quality (GitHub/Bitbucket)](https://img.shields.io/scrutinizer/quality/g/serchaofan/oakleaf/master)
![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/serchaofan/oakleaf)

</center>

oakleaf 目前支持命令

- get
  - hosts
  - groups
- run
  - ping
  - command
  - script
  - sysinfo
  - loadinfo
  - download

## 使用手册

### 配置hosts文件
```
[test]
root@192.168.10.139=0okm(IJN8uhb
```

### 基础使用
```
$ python oakleaf.py
usage: oakleaf [-h]  ...

Oakleaf Is An Ops Tool , Writen In Python.

optional arguments:
  -h, --help  show this help message and exit

Oakleaf Sub Command:

    get       Get Infomation
    run       Execute Scripts and Commands on target servers
```

#### get
```
$ python oakleaf.py get
usage: get [-h]  ...

positional arguments:

    hosts (ho)  Get Hosts Info
    groups (gro)
                Get Groups Info
```
- hosts
  ```
  $ python oakleaf.py get hosts
  GROUP   HOSTIP          SSHPORT USER            PASSWORD
  test    192.168.10.139  22      root            0okm(IJN8uhb
  local   192.168.60.17   22      root            redhat
  ```
- groups
  ```
  $ python oakleaf.py get groups
  GROUP           HOSTS
  test            1
  local           1
  ```
#### run
```
$ python oakleaf.py run
usage: oakleaf run [-h]  ...

positional arguments:

    ping      Ping hosts
    command   Run Command on Hosts
    script    Run Script on Hosts
    copy      Copy Files to Hosts
    file      Set File's Properties on Hosts
    sysinfo   Get System Info from Hosts
    loadinfo  Get System Load Info from Hosts
    chpass    Change Password of Hosts
    download  Download Files on Remote Host
```
- ping
  ```
  $ python oakleaf.py run ping -A
  [192.168.10.139 >> uname -s]
  [+] 192.168.10.139 Success 493ms
  [192.168.60.17 >> uname -s]
  [-] 192.168.60.17 UnReachable 2000ms
  Reason: timed out
  ```
- command
  ```
  $ python oakleaf.py run command -g test echo hello world
  [192.168.10.139 >> echo hello world]
  [+] 192.168.10.139 Success 528ms
  Stdout: hello world
  ```
- script
  ```
  $ python oakleaf.py run script -f scripts\sysinfo -g test
  [192.168.10.139 >> scripts\sysinfo]
  [+] 192.168.10.139 Success 666ms remote: /tmp/sysinfo
  [192.168.10.139 >> chown -R root:root /tmp/sysinfo]
  [+] 192.168.10.139 Success 707ms
  [192.168.10.139 >> chmod -R 754 /tmp/sysinfo]
  [+] 192.168.10.139 Success 886ms
  [192.168.10.139 >> /bin/sh /tmp/sysinfo ]
  [+] 192.168.10.139 Success 599ms
  Stdout: 
  CPU Info >>>
      Model:        Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz
      Frequency:    2000.000MHz
      Cache:        15360 KB
      Process Count: 6
  ......
  ```
- copy
  ```
  $ python oakleaf.py run copy -f scripts\sysinfo -g test -d /tmp/ -o root -p 777
  [192.168.10.139 >> scripts\sysinfo]
  [+] 192.168.10.139 Success 657ms remote: /tmp/sysinfo
  [192.168.10.139 >> chown -R root:root /tmp/sysinfo]
  [+] 192.168.10.139 Success 526ms
  [192.168.10.139 >> chmod -R 777 /tmp/sysinfo]
  [+] 192.168.10.139 Success 517ms
  ```
- file
  ```
  $ python oakleaf.py run file -f /tmp/sysinfo -g test -o root -p 777
  [192.168.10.139 >> chown -R root:root /tmp/sysinfo]
  [+] 192.168.10.139 Success 680ms
  [192.168.10.139 >> chmod 777 /tmp/sysinfo]
  [+] 192.168.10.139 Success 553ms
  ```
- sysinfo
  ```
  $ python oakleaf.py run sysinfo -g test
  [192.168.10.139 >> yum install -y curl]
  [+] 192.168.10.139 Success 131ms
  [192.168.10.139 >> curl -O -k -L https://raw.githubusercontent.com/serchaofan/laogu-scripts/master/scripts/shell/info/sysinfo.sh]

  [+] 192.168.10.139 Success 168ms
  [192.168.10.139 >> chmod +x ~/sysinfo.sh]
  [+] 192.168.10.139 Success 509ms
  [192.168.10.139 >> sh ~/sysinfo.sh]
  [+] 192.168.10.139 Success 572ms
  Stdout:
  CPU Info >>>
      Model:        Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz
      Frequency:    2000.000MHz
      Cache:        15360 KB
      Process Count: 6
  .......
  ```
- loadinfo
  ```
  $ python oakleaf.py run loadinfo -g test
  [192.168.10.139 >> yum install -y curl]
  [+] 192.168.10.139 Success 134ms
  [192.168.10.139 >> curl -O -k -L https://raw.githubusercontent.com/serchaofan/laogu-scripts/master/scripts/shell/info/loadinfo.sh]
  [+] 192.168.10.139 Success 129ms
  [192.168.10.139 >> chmod +x ~/loadinfo.sh]
  [+] 192.168.10.139 Success 515ms
  [192.168.10.139 >> sh ~/loadinfo.sh]
  [+] 192.168.10.139 Success 643ms
  Stdout: =======================================================
  Kernel Version: 3.10.0-957.el7.x86_64
  HostName:       ci-test
  =======================================================
  Interface       IP Address
  ens192          192.168.10.139/24
  docker0         172.17.0.1/16
  br-cb3029830afb         172.18.0.1/16
  ......
  ```
- download
  ```
  $ python oakleaf.py run download -g test --url https://raw.githubusercontent.com/serchaofan/laogu-scripts/master/scripts/shell/info/loadinfo.sh
  [192.168.10.139 >> yum install -y curl]
  [+] 192.168.10.139 Success 376ms
  [192.168.10.139 >> curl -O -k -L https://raw.githubusercontent.com/serchaofan/laogu-scripts/master/scripts/shell/info/loadinfo.sh]
  [+] 192.168.10.139 Success 787ms
  ```