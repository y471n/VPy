import zipfile
from threading import Thread


def extract_file(zFile, password):
    try:
        zFile.extractall(pwd=bytes(password, encoding='utf-8'))
        print('[+] Password = ' + password + '\n')
    except Exception as e:
        # print("Tried:"+password+"\n")
        # print(e)
        pass


def main():
    z_file = zipfile.ZipFile('evil.zip')
    print(type(z_file))
    pass_file = open('dictionary.txt')
    for line in pass_file:
        password = line.strip("\n")
        t = Thread(target=extract_file, args=(z_file, password))
        t.start()


if __name__ == '__main__':
    main()
