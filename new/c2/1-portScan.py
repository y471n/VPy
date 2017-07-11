import optparse
from _socket import gethostbyname, gethostbyaddr, setdefaulttimeout, socket, \
    AF_INET, SOCK_STREAM


def port_scan(target_host, target_ports):
    try:
        target_ip = gethostbyname(target_host)
    except:
        print("[-] Cannot resolve %s : Unknown host".format(target_host))
        return
    try:
        target_name = gethostbyaddr(target_ip)
        print('\n[+] Scan Results for: ' + target_name)
    except:
        print('\n[+] Scan Results for: ' + target_ip)

    setdefaulttimeout(1)

    for target_port in target_ports:
        print('Scanning port ' + target_port)
        connection_scan(target_host, int(target_port))


def connection_scan(target_host, target_port):
    try:
        connection_socket = socket(AF_INET, SOCK_STREAM)
        connection_socket.connect((target_host, target_port))
        connection_socket.send('Vpy\r\n')
        results = connection_socket.recv(100)
        print('[+]%d/tcp open' % target_port)
        print('[+] ' + str(results))
        connection_socket.close()
    except:
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
