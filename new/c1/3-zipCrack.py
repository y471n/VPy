import zipfile
from threading import Thread
import optparse


def extract_file(zFile, password):
    try:
        zFile.extractall(pwd=bytes(password, encoding='utf-8'))
        print('[+] Password = ' + password + '\n')
    except:
        pass


def main():
    parser = optparse.OptionParser("usage%prog " + "-f <zip_file> -d "
                                                   "<dictionary>")
    parser.add_option('-f', dest='zname', type='string', help='specify zip '
                                                               'file')
    parser.add_option('-d', dest='dname', type='string', help='specify '
                                                            'dictionary file')
    (options, args) = parser.parse_args()

    if (options.zname is None) | (options.dname is None):
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname

    z_file = zipfile.ZipFile(zname)
    pass_file = open(dname)
    for line in pass_file:
        password = line.strip("\n")
        t = Thread(target=extract_file, args=(z_file, password))
        t.start()


if __name__ == '__main__':
    main()
