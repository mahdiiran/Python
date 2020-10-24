import os
print('\n\nping calcultor\ndeveloper:seyedmahdi moosavian\ncopy right2020 All rights reserved\nbuy our apps in: https://idpay.ir/camputerland/file')
print('\n\n1. 8.8.8.8\n2. 1.1.1.1\n3. 208.67.222.222\n4. 208.67.220.220\n5. 185.55.225.25\n6. 4.2.2.6\n7. 178.22.122.100\n8. 94.232.174.194\n9. 194.225.152.10\n10. 8.8.4.4\n11. 156.154.71.1\n12. 4.2.2.5\n13. 24.113.32.29\n14. 204.194.234.200\n15. Custom IP')
while 5!=1:
    ping=input('Please type your choice(1-15) for pinging:')
    if ping=='1':
        os.system('ping 8.8.8.8 -t')
    elif ping=='2':
        os.system('ping 1.1.1.1 -t')
    elif ping=='3':
        os.system('ping ModemIP -t')
    elif ping=='4':
        os.system('ping 208.67.220.220 -t')
    elif ping=='5':
        os.system('ping 185.55.225.25 -t')
    elif ping=='6':
        os.system('ping 4.2.2.6 -t')
    elif ping=='7':
        os.system('ping 178.22.122.100 -t')
    elif ping=='8':
        os.system('ping 94.232.174.194 -t')
    elif ping=='9':
        os.system('ping 194.225.152.10 -t')
    elif ping=='10':
        os.system('ping 8.8.4.4 -t')
    elif ping=='11':
        os.system('ping 156.154.71.1 -t')
    elif ping=='12':
        os.system('ping 4.2.2.5 -t')
    elif ping=='13':
        os.system('ping 24.113.32.29 -t')
    elif ping=='14':
        os.system('ping 204.194.234.200 -t')
    elif ping=='15':
        custom=input('type custom IP:')
        os.system('ping '+custom+' -t')
    else:
        print('the value is out of range!\n')