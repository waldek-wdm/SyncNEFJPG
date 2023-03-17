__author__ = 'plr01183'

import os.path, sys
#from os import system
from os import listdir as ls
from pprint import pprint
from shutil import copyfile

pathname = os.path.dirname(sys.argv[0])
#print pathname
sciezka_source = pathname + '\\source\\'
sciezka_dest = pathname + '\\dest\\'
sciezka_removed = pathname + '\\removed\\'

#print sciezka_source

try:
    if not os.path.isdir('sciezka_removed'):
        os.makedirs(sciezka_removed)
except:
    WindowsError

try:
    if not os.path.isdir('sciezka_source'):
        os.makedirs(sciezka_source)
except:
    WindowsError

try:
    if not os.path.isdir('sciezka_dest'):
        os.makedirs(sciezka_dest)
except:
    WindowsError

pliki_source = ls(sciezka_source)
print pliki_source
wszystkie_pliki = ls(pathname)
for pliki_glowne in wszystkie_pliki:
    if '.par' in pliki_glowne:
        copyfile(pathname + '\\' + pliki_glowne, sciezka_dest + pliki_glowne)
        os.remove(pathname + '\\' + pliki_glowne)
    if '.dum' in pliki_glowne:
        copyfile(pathname +'\\'+ pliki_glowne, sciezka_source + pliki_glowne)
        os.remove(pathname +'\\'+ pliki_glowne)

for nr_source in pliki_source:
    print nr_source
    source_plik = nr_source.rstrip('.dum\r\n')
    print source_plik
    dest_plik = source_plik + '.par'
    print dest_plik
    if not os.path.isfile(sciezka_dest + dest_plik):
        copyfile(sciezka_source + nr_source, sciezka_removed + nr_source)
        os.remove( sciezka_source + nr_source)
