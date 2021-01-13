# mapIT.py
# launch maps.google.com with specific address

import webbrowser
import sys
import pyperclip
import argparse
import smtplib
import bs4
import requests

def get_map (information):
    if information != None:
        address = ' '.join(information)
    else:
        address = pyperclip.paste()
    webbrowser.open('https://www.google.com/maps/place/' + address)
    s = ' '.join(address).encode('utf-8')
    return(s)

def mailing_smtp(addr):
    smtpObj = smtplib.SMTP('smtp.gmail.com',587)
    s = smtpObj.ehlo()
    print(s)
    s = smtpObj.starttls()
    print(s)
    usr_id = 'mafirst1011@gmail.com'
    print('Password:')
    try:
        usr_pwd = input()
        s = smtpObj.login(usr_id,usr_pwd)
        print(s)
        rep_id = 'viet.hoang@p-square.de'
        print('Subject:')
        sub_ject = 'Dear MF\n' + 'This is requested address:' + addr + '\n\n Mfg, \n\n Kanard'  
        s = smtpObj.sendmail(usr_id,rep_id,sub_ject)
        print(s)
    except:
        print('No input password')
    s = smtpObj.quit()
    print(s)


# TODO soup.select not working

def search_gg(input):
    print('Googling...')
    res = requests.get('https://google.com/search?q=' + ' '.join(input))
    print(res)
    res.raise_for_status()
    print(res.text)
    soup = bs4.BeautifulSoup(res.text,features="html.parser")
    linkElems = soup.select('.r a')
    print(linkElems)
    numOpen = min(5,len(linkElems))
    print(numOpen)
    for i in range(numOpen):
        webbrowser.open('http://google.com' + linkElems[i].get('href'))


def download_comic():
    print('Comic from XKCD')


if __name__ == '__main__':
    
    print('Web automation application')
    try:
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('--maps', type=str, nargs='+',help='search and open locations')
        parser.add_argument('--search', type=str,nargs='+', help='')
        parser.add_argument('--comic',type=str,nargs='+',help='download new comics')
        args = parser.parse_args()
    except IOError:
        print('IO Error')
    except:
        print('Unidentified Error')
        sys.exit(1)

    s =''
    if args.maps != None:
        s = get_map(args.maps)
        print('Process complete')
        print('Sending addresse to Email')
        mailing_smtp(s)
    if args.search != None:
        search_gg(args.search)
    if args.comic == None:
        download_comic()

    print('Program completed')