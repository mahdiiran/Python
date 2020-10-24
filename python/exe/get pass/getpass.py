import os
ssid = input('Type WIFI SSID:')
os.system('Netsh Wlan Show Profiles '+ssid+' Key=Clear')
c = input('press enter to close program')
