import optparse
from socket import gethostbyname, gethostbyaddr, setdefaulttimeout, socket, \
    AF_INET, SOCK_STREAM


def port_scan(target_host, target_ports):
    try:
        target_ip = gethostbyname(target_host)
    except:
        print("[-] Cannot resolve %s : Unknown host".format(target_host))
        return
    print(type(target_ip))
    target_host = target_ip
    try:
        target_name = gethostbyaddr(target_ip)
        if isinstance(target_name, str):
            print('\n[+] Scan Results for: ' + target_name)
    except Exception as e:
        print(e)
        print('\n[+] Scan Results for: ' + target_ip)
    print(target_ip, target_host, target_name)
    setdefaulttimeout(40)

    for target_port in target_ports:
        print('Scanning port ' + target_port)
        tcp_connect_scan(target_host, int(target_port))


def tcp_connect_scan(target_host, target_port):
    try:
        connection_socket = socket(AF_INET, SOCK_STREAM)
        connection_socket.connect((target_host, target_port))
        connection_socket.send('ViolentPy\r\n')
        results = connection_socket.recv(100)
        print('[+]%d/tcp open' % target_port)
        print('[+] ' + str(results))
        connection_socket.close()
    except Exception as e:
        print(e)
        print('[-]%d/tcp closed' % target_port)


def main():
    parser = optparse.OptionParser("usage%prog " +
                                   " -H <target_host>" +
                                   " -p <target_port>")
    parser.add_option('-H', dest='tgt_host', type='string', help='Specify '
                                                                 'target host')
    parser.add_option('-p', dest='tgt_port', type='string', help='Specify '
                                                                 'target '
                                                                 'port[s] '
                                                                 'separated '
                                                                 'by comma')

    (options, args) = parser.parse_args()
    target_host = options.tgt_host
    target_ports = str(options.tgt_port).split(',')

    if (target_host is None) | (target_ports is None):
        print('[-] You must specify a target host and port[s]')
        exit(0)

    port_scan(target_host, target_ports)


if __name__ == '__main__':
    main()
