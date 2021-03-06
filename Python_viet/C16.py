# send_mail check_mail

import smtplib
import imapclient
import pprint
import sys
# import pyzmail

def mailing_smtp():
    smtpObj = smtplib.SMTP('smtp.gmail.com',587)
    s = smtpObj.ehlo()
    print(s)
    s = smtpObj.starttls()
    print(s)
    print('User Email:')
    usr_id = input()
    print('Password:')
    usr_pwd = input()
    s = smtpObj.login(usr_id,usr_pwd)
    print(s)
    print('Recipient Email:')
    rep_id = input()
    print('Subject:')
    sub_ject = input()
    s = smtpObj.sendmail(usr_id,rep_id,sub_ject)
    print(s)
    s = smtpObj.quit()
    print(s)

def recv_imap():
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    print('User Email:')
    usr_id = input()
    print('Password:')
    usr_pwd = input()
    s = imapObj.login(usr_id,usr_pwd)
    print(s)
    pprint.pprint(imapObj.list_folders())
    print('Access which folder:')
    fol = input()
    s = imapObj.select_folder(fol,readonly=True)
    print(s)
    print('Wanna search anything?')
    s = input()
    s = imapObj.search(['ALL'])
    print(s)
    print('which mail?')
    UID = input()
    print(UID)
    raw_mess = imapObj.fetch([UID],['BODY[]','FLAGS'])
    print(raw_mess)
    # mess = pyzmail.PyzMessage.factory(raw_mess[UID]['BODY[]'])
    # print(mess + ' ' + mess.get_subject() + ' ' + mess.get_addresses('from') + ' ' + mess.get_addresses('to'))
    s = imapObj.logout()
    print(s)
    
if __name__ == '__main__': 
    n = True
    while n:
        print('send_mail or check_mail')
        i = input()
        if i == 'send_mail':
            mailing_smtp()
        elif i == 'check_mail':
            recv_imap()
        else:
            print('Quit?(Y/n)')
            s = input()
            if s == 'Y':
                sys.exit(1)
            elif s == 'n':
                continue
