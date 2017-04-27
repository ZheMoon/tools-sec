import zipfile
import argparse
from threading import Thread


def extractFile(zFile, password):
    try:
        password = bytes(password, encoding='utf-8')
        zFile.extractall(pwd=password)
        print("[+] Found password {}".format(str(password)))
    except:
        pass


def main():
    description = "usage%prog -f <zipfile> -d <dictionary>"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-f', dest='zname', type=str, help='specify zip file')
    parser.add_argument('-d', dest='dname', type=str, help='specify dictionary\
 file')
    args = parser.parse_args()
    if (args.zname is None) | (args.dname is None):
        print(parser.print_help())
        exit(0)
    else:
        zname = args.zname
        dname = args.dname

    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip("\n")
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()


if __name__ == '__main__':
    main()
