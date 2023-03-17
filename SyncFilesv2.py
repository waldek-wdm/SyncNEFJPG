__author__ = 'plr01183'

import os.path, sys
from string import upper
from os import system
from os import listdir as ls
from pprint import pprint
from shutil import copyfile

#pathname = os.path.dirname(sys.argv[0])
pathname = os.path.abspath(os.path.dirname(__file__))
sciezka_source = os.path.join(pathname, 'NEF\\')
sciezka_dest = os.path.join(pathname, 'JPG\\')
sciezka_removed = os.path.join(pathname, 'removed\\')
print pathname
print sciezka_source
print sciezka_dest
print sciezka_removed

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
print pathname
wszystkie_pliki = ls(pathname)
for pliki_glowne in wszystkie_pliki:
    pliki_glowne = pliki_glowne.upper()
    #print pliki_glowne
    if '.JPG' in pliki_glowne:
        copyfile(pathname + '\\' +  pliki_glowne, sciezka_dest + pliki_glowne)
        os.remove(pathname + '\\' +  pliki_glowne)
    if '.NEF' in pliki_glowne:
        copyfile(pathname + '\\' + pliki_glowne, sciezka_source + pliki_glowne)
        os.remove(pathname + '\\' + pliki_glowne)

#pliki_source = ls(sciezka_source)

for nr_source in pliki_source:
    name = nr_source.rstrip('.NEF\r\n')
    dest_plik = name + '.JPG'
    if not os.path.isfile(sciezka_dest + dest_plik):
        copyfile(sciezka_source + nr_source, sciezka_removed + nr_source)
        os.remove( sciezka_source + nr_source)
