import os
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 autoTOR.py')
    run('mkdir /usr/share/iftor')
    run('cp autoTOR.py /usr/share/iftor/autoTOR.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/iftor/autoTOR.py "$@"')
    with open('/usr/bin/iftor','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/iftor & chmod +x /usr/share/iftor/autoTOR.py')
    print('''\n\ncongratulation IEHF auto Tor Ip Changer is installed successfully \nfrom now just type \x1b[6;30;42maut\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/iftor ')
    run('rm /usr/bin/iftor ')
    print('[!] now IEHF Auto Tor Ip changer  has been removed successfully')
