# uncompyle6 version 3.6.7
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Jul  8 2020, 22:53:57) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <febry>
import os, re, requests, json, urllib, random, sys
from time import sleep, strftime, localtime
from bs4 import BeautifulSoup as sop
from requests.exceptions import ConnectionError as legh
bl = '\x1b[0;34m'
dg = '\x1b[1;30m'
lb = '\x1b[1;34m'
lg = '\x1b[1;32m'
lc = '\x1b[1;36m'
lr = '\x1b[1;31m'
lp = '\x1b[1;35m'
yw = '\x1b[1;33m'
wh = '\x1b[1;37m'
no = '\x1b[0m'
bold = '\x1b[1m'
under = '\x1b[4m'

def banner():
    os.system('clear')
    print yw + '' + bold + wh + '| ' + lg + '<[[[=[[ Tuyul Google ]]=]]]>'
    print yw + '' + bold + wh + '| ' + lg + 'Tools Scanning Proxy Universitas'
    print yw + '' + bold + wh + '| ' + lg + 'https://tuyul-google.blogspot.com\n' + wh


def pas1():
    os.system('clear')
    os.system('touch pas.txt')
    wkt = strftime('%d', localtime())
    file = open('pas.txt', 'w')
    file.write(str(wkt) + '1234')
    file.close()
    pas2()


def pas2():
    banner()
    tour = open('pas.txt')
    jedug = open('session.txt')
    tour = tour.read()
    jedug = jedug.read()
    if str(jedug) == str(tour):
        os.system('clear')
        os.system('rm -rf pas.txt')
        rest()
    else:
        banner()
        os.system('rm -rf pas.txt')
        salah()


def salah():
    print lr + '[!] ' + wh + 'Access Token Sudah Expire !'
    print lr + '[\xe2\x80\xa2] ' + wh + 'Masukan Kembali Access Token..'
    jays = raw_input(lr + '[?] ' + wh + 'Access Token ' + lr + '>>' + wh + ' ')
    tired = open('session.txt', 'w')
    tired.write(jays)
    tired.close()
    pas1()


def new():
    try:
        nyenye = open('session.txt')
        nyenye.close()
        pas1()
    except IOError:
        try:
            os.system('clear')
            banner()
            os.system('touch session.txt')
            print lr + '[+] ' + lc + '<[[[=[[WELCOME]]=]]]>'
            fix = raw_input(lr + '[?]' + wh + ' Access Token' + lr + ' >>' + wh + ' ')
            bre = open('session.txt', 'w')
            bre.write(fix)
            bre.close()
            pas1()
        except KeyboardInterrupt:
            print lr + '[!] ' + wh + 'Exit..\n'
            sys.exit()


def main():
    try:
        os.system('clear')
        banner()
        print lr + '[\xe2\x80\xa2] ' + wh + 'Ex: ' + wh + '111.223.252'
        ip = raw_input(lr + '[?] ' + wh + 'Proxy ' + lr + '>>' + wh + ' ')
        port = raw_input(lr + '[?] ' + wh + 'Port  ' + lr + '>>' + wh + ' ')
        print lr + '[+] ' + wh + 'Start Checking..\n'
    except KeyboardInterrupt:
        print lr + '[!] ' + bold + wh + 'Exit..\n'
        sys.exit()

    os.system('touch open.txt')
    os.system('touch close.txt')
    os.system('touch good.txt')
    sk = open('good.txt', 'w')
    op = open('open.txt', 'w')
    cl = open('close.txt', 'w')
    a = 0
    wkt = strftime('%H:%M', localtime())
    while a <= 255:
        try:
            ngab = requests.get('http://' + ip + '.' + str(a) + ':' + port, timeout=2)
            pr = ip + '.' + str(a) + ':' + port
            jos = ngab.status_code
            if ngab.status_code == 200:
                print wh + '[' + lg + wkt + wh + '] ' + lc + pr + wh + ' is ' + lg + 'open (200)'
                a += 1
                op.write(pr + '\n')
            elif ngab.status_code == 301:
                print wh + '[' + lg + wkt + wh + '] ' + lc + pr + wh + ' is ' + lg + 'open (301)'
                a += 1
                op.write(pr + '\n')
            elif ngab.status_code == 307:
                print wh + '[' + lg + wkt + wh + '] ' + lc + pr + wh + ' is ' + lg + 'open (307)'
                a += 1
                op.write(pr + '\n')
            elif ngab.status_code == 404:
                print wh + '[' + lg + wkt + wh + '] ' + lc + pr + wh + ' is ' + lg + 'open'
                a += 1
                op.write(pr + '\n')
            elif ngab.status_code == 302:
                print wh + '[' + lg + wkt + wh + '] ' + lc + pr + wh + ' is ' + lg + 'open (302)'
                a += 1
                op.write(pr + '\n')
            elif ngab.status_code == 403:
                print wh + '[' + lg + wkt + wh + '] ' + lc + pr + wh + ' is ' + lr + 'close (403)'
                a += 1
                cl.write(pr + '\n')
            elif ngab.status_code == 401:
                print wh + '[' + lg + wkt + wh + '] ' + lc + pr + wh + ' is ' + yw + 'bagus (401)'
                a += 1
                sk.write(pr + '\n')
            elif ngab.status_code == 503:
                print wh + '[' + lg + wkt + wh + '] ' + lc + pr + wh + ' is ' + lg + 'open (503)'
                a += 1
                op.write(pr + '\n')
            elif ngab.status_code == 508:
                print wh + '[' + lg + wkt + wh + '] ' + lc + pr + wh + ' is ' + lg + 'open'
                a += 1
                op.write(pr + '\n')
            else:
                print wh + '[' + lg + wkt + wh + '] ' + lc + pr + wh + ' is ' + lg + 'open'
                a += 1
                op.write(pr + '\n')
        except requests.exceptions.Timeout:
            a += 1
            print wh + '[' + lg + wkt + wh + '] ' + lc + ip + '.' + str(a) + ':' + port + wh + ' is ' + lr + 'close'
            cl.write(ip + '.' + str(a) + ':' + port + '\n')
            continue
        except legh:
            a += 1
            print wh + '[' + lg + wkt + wh + '] ' + lc + ip + '.' + str(a) + ':' + port + wh + ' is ' + lr + 'close'
            cl.write(ip + '.' + str(a) + ':' + port + '\n')
            continue
        except KeyboardInterrupt as ex:
            cl.close()
            op.close()
            sk.close()
            erere()
        except Exception as Er:
            print Er


def erere():
    jum = open('open.txt', 'r')
    jom = open('close.txt', 'r')
    jim = open('good.txt', 'r')
    jim = jim.readlines()
    jum = jum.readlines()
    jom = jom.readlines()
    print lg + '\n     Hidup' + wh + ': ' + str(len(jum)) + lr + ' Coid' + wh + ': ' + str(len(jom)) + yw + ' Bagus:' + wh + ' ' + str(len(jim)) + '\n'
    os.system('rm -rf close.txt')
    kaus = raw_input('    [ ' + lp + 'Tekan Enter Untuk Kembali ' + wh + ']')
    rest()


def menu():
    try:
        banner()
        print '[' + lc + '01' + wh + '] Univers Institut Teknologi Bandung'
        print '[' + lc + '02' + wh + '] Univers Gadjah Mada'
        print '[' + lc + '03' + wh + '] Univers Institut Pertanian Bogor'
        print '[' + lc + '04' + wh + '] Univers Pendidikan Indonesia'
        print '[' + lc + '05' + wh + '] Univers Pancasila'
        print '[' + lc + '06' + wh + '] Univers Diponegoro'
        print '[' + lc + '07' + wh + '] Univers Sebelas Maret'
        print '[' + lc + '08' + wh + '] Univers Brahwijaya'
        print '[' + lc + '09' + wh + '] Univers Negeri Jakarta'
        print '[' + lc + '10' + wh + '] Univers Airlangga'
        print '[' + lc + '11' + wh + '] Univers Terbuka'
        print '[' + lc + '12' + wh + '] Univers Padjadjaran'
        print '[' + lc + '13' + wh + '] Univers Negeri Yogyakarta'
        print '[' + lc + '14' + wh + '] Univers Gunadarma'
        print '[' + lc + '15' + wh + '] Univers Jendral Soedirman'
        print '[' + lc + '16' + wh + '] Univers Udayana'
        print '[' + lc + '17' + wh + '] Univers Sriwijaya'
        print '[' + lc + '18' + wh + '] Univers Andalas'
        print '[' + lc + '19' + wh + '] Univers Pelita Harapan'
        print '[' + lc + '20' + wh + '] Univers Pembangunan Nasional'
        print '[' + lc + '21' + wh + '] Univers Negeri Surabaya'
        print '[' + lc + '22' + wh + '] Univers Negeri Malang'
        print '[' + lc + '23' + wh + '] Univers Pamulang'
        print '[' + lc + '24' + wh + '] Univers Islam Bandung'
        print '[' + lc + '25' + wh + '] Univers Negeri Padang'
        print '\n[' + lc + '00' + wh + '] Back\n'
        o = raw_input(lr + '[?] ' + wh + 'Choice ' + lr + '>>' + wh + ' ')
        if o == '01' or o == '1':
            ip = '167.205.1'
            nama = 'Institut Teknologi Bandung'
            auto(ip, nama)
        elif o == '02' or o == '2':
            ip = '175.111.88'
            nama = 'Gadjah Mada'
            auto(ip, nama)
        elif o == '03' or o == '3':
            ip = '202.124.205'
            nama = 'Institut Pertanian Bogor'
            auto(ip, nama)
        elif o == '04' or o == '4':
            ip = '103.23.244'
            nama = 'Pendidikan Indonesia'
            auto(ip, nama)
        elif o == '05' or o == '5':
            ip = '202.43.95'
            nama = 'Pancasila'
            auto(ip, nama)
        elif o == '06' or o == '6':
            ip = '182.255.1'
            nama = 'Diponegoro'
            auto(ip, nama)
        elif o == '07' or o == '7':
            ip = '203.6.148'
            nama = 'Sebelas Maret'
            auto(ip, nama)
        elif o == '08' or o == '8':
            ip = '175.45.184'
            nama = 'Brahwijaya'
            auto(ip, nama)
        elif o == '09' or o == '9':
            ip = '103.8.12'
            nama = 'Negeri Jakarta'
            auto(ip, nama)
        elif o == '10':
            ip = '210.57.214'
            nama = 'Airlangga'
            auto(ip, nama)
        elif o == '11':
            ip = '203.217.140'
            nama = 'Terbuka'
            auto(ip, nama)
        elif o == '12':
            ip = '111.223.252'
            nama = 'Padjadjaran'
            auto(ip, nama)
        elif o == '13':
            ip = '101.203.168'
            nama = 'Negeri Yogyakarta'
            auto(ip, nama)
        elif o == '14':
            ip = '104.237.55'
            nama = 'Gunadarma'
            auto(ip, nama)
        elif o == '15':
            ip = '103.9.22'
            nama = 'Jendral Soedirman'
            auto(ip, nama)
        elif o == '16':
            ip = '103.29.196'
            nama = 'Udayana'
            auto(ip, nama)
        elif o == '17':
            ip = '103.241.4'
            nama = 'Sriwijaya'
            auto(ip, nama)
        elif o == '18':
            ip = '103.212.43'
            nama = 'Andalas'
            auto(ip, nama)
        elif o == '19':
            ip = '122.200.10'
            nama = 'Pelita Harapan'
            auto(ip, nama)
        elif o == '20':
            ip = '103.236.192'
            nama = 'Pembangunan Nasional'
            auto(ip, nama)
        elif o == '21':
            ip = '103.242.124'
            nama = 'Negeri Surabaya'
            auto(ip, nama)
        elif o == '22':
            ip = '202.52.137'
            nama = 'Negeri Malang'
            auto(ip, nama)
        elif o == '23':
            ip = '202.137.16'
            nama = 'Pamulang'
            auto(ip, nama)
        elif o == '24':
            ip = '103.78.195'
            nama = 'Islam Bandung'
            auto(ip, nama)
        elif o == '25':
            ip = '103.216.87'
            nama = 'Negeri Padang'
            auto(ip, nama)
            auto(ip, nama)
        elif o == '00':
            rest()
        else:
            print '[!] Perintah Salah...'
    except Exception as err:
        print lr + '[!] ' + wh + 'Periksa Jaringan Internet...\n'
        sys.exit()
    except KeyboardInterrupt:
        print lr + '[!] ' + wh + 'Exit..'


def rest():
    try:
        os.system('clear')
        banner()
        print '[' + lc + '1' + wh + '] Scanning Proxy Auto'
        print '[' + lc + '2' + wh + '] Scanning Proxy Manual'
        print '[' + lc + '3' + wh + '] Exit\n'
        oalah = raw_input(lr + '[?] ' + wh + 'Choice ' + lr + '>>' + wh + ' ')
        if oalah == '1':
            os.system('clear')
            menu()
        elif oalah == '2':
            os.system('clear')
            main()
        elif oalah == '3':
            print lr + '[\xe2\x80\xa2] ' + wh + 'Sampai Jumpa Lagi...\n'
            sys.exit()
        else:
            print lr + '[!] ' + wh + 'Perintah Salah...'
            sleep(1.5)
            os.system('clear')
            rest()
    except KeyboardInterrupt:
        print lr + '[!] ' + wh + 'Exit..\n'
        sys.exit()
    except Exception as err:
        print lr + '\n[!] ' + wh + 'Error 404\n'
        rest()


def auto(ip, nama):
    try:
        os.system('clear')
        banner()
        print lr + '[\xe2\x80\xa2] ' + wh + 'Universitas ' + nama
        print lr + '[\xe2\x80\xa2] ' + wh + 'Proxy ' + lr + '>>' + wh + ' ' + ip
        port = raw_input(lr + '[\xe2\x80\xa2] ' + wh + 'Port  ' + lr + '>>' + wh + ' ')
        print lr + '[+] ' + wh + 'Start Checking..\n'
    except KeyboardInterrupt:
        print lr + '[!] ' + bold + wh + 'Exit..\n'
        sys.exit()

    os.system('touch open.txt')
    os.system('touch close.txt')
    os.system('touch good.txt')
    sk = open('good.txt', 'w')
    op = open('open.txt', 'w')
    cl = open('close.txt', 'w')
    a = 0
    wkt = strftime('%H:%M', localtime())
    while a <= 255:
        try:
            ngab = requests.get('http://' + ip + '.' + str(a) + ':' + port, timeout=2)
            pr = ip + '.' + str(a) + ':' + port
            jos = ngab.status_code
            if ngab.status_code == 200:
                print wh + '[' + lg + wkt + wh + '] ' + lc + pr + wh + ' is ' + lg + 'open (200)'
                a += 1
                op.write(pr + '\n')
            elif ngab.status_code == 301:
                print wh + '[' + lg + wkt + wh + '] ' + lc + pr + wh + ' is ' + lg + 'open (301)'
                a += 1
                op.write(pr + '\n')
            elif ngab.status_code == 307:
                print wh + '[' + lg + wkt + wh + '] ' + lc + pr + wh + ' is ' + lg + 'open (307)'
                a += 1
                op.write(pr + '\n')
            elif ngab.status_code == 404:
                print wh + '[' + lg + wkt + wh + '] ' + lc + pr + wh + ' is ' + lg + 'open'
                a += 1
                op.write(pr + '\n')
            elif ngab.status_code == 302:
                print wh + '[' + lg + wkt + wh + '] ' + lc + pr + wh + ' is ' + lg + 'open (302)'
                a += 1
                op.write(pr + '\n')
            elif ngab.status_code == 403:
                print wh + '[' + lg + wkt + wh + '] ' + lc + pr + wh + ' is ' + lr + 'close (403)'
                a += 1
                cl.write(pr + '\n')
            elif ngab.status_code == 401:
                print wh + '[' + lg + wkt + wh + '] ' + lc + pr + wh + ' is ' + yw + 'good (401)'
                a += 1
                sk.write(pr + '\n')
            elif ngab.status_code == 503:
                print wh + '[' + lg + wkt + wh + '] ' + lc + pr + wh + ' is ' + lg + 'open (503)'
                a += 1
                op.write(pr + '\n')
            elif ngab.status_code == 508:
                print wh + '[' + lg + wkt + wh + '] ' + lc + pr + wh + ' is ' + lg + 'open'
                a += 1
                op.write(pr + '\n')
            else:
                print wh + '[' + lg + wkt + wh + '] ' + lc + pr + wh + ' is ' + lg + 'open'
                a += 1
                op.write(pr + '\n')
        except requests.exceptions.Timeout:
            a += 1
            print wh + '[' + lg + wkt + wh + '] ' + lc + ip + '.' + str(a) + ':' + port + wh + ' is ' + lr + 'close'
            cl.write(ip + '.' + str(a) + ':' + port + '\n')
            continue
        except legh:
            a += 1
            print wh + '[' + lg + wkt + wh + '] ' + lc + ip + '.' + str(a) + ':' + port + wh + ' is ' + lr + 'close'
            cl.write(ip + '.' + str(a) + ':' + port + '\n')
            continue
        except KeyboardInterrupt as ex:
            cl.close()
            op.close()
            sk.close()
            erere()
        except Exception as Er:
            print Er


if __name__ == '__main__':
    new()
    erere()
