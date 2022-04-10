import urllib.request


try:
   site = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('\033[1;31mO site Pudim não está acessivel.\033[m')
else:
    print('\033[1;32mO site Pudim está acessivel\033[m')
