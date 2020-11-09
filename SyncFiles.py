__author__ = 'plr01183'

import os.path
#from os import system
from os import listdir as ls
from pprint import pprint
from shutil import copyfile

sciezka_source = 'source\\'
sciezka_dest = 'dest\\'
sciezka_removed = 'removed\\'

pliki_source = ls(sciezka_source)
pliki_dest = ls(sciezka_dest)

try:
    if not os.path.isdir('sciezka_removed'):
        os.makedirs(sciezka_removed)

except:
    WindowsError

for nr_source in pliki_source:
    source_plik = nr_source.rstrip('.dum\r\n')
    istnieje = 0
    for nr_dest in pliki_dest:
        dest_plik = nr_dest.rstrip('.par\r\n')
        print source_plik
        if source_plik == dest_plik:
            print dest_plik
            istnieje = 1
    if istnieje == 0:
        copyfile(sciezka_source + nr_source, sciezka_removed + nr_source)
        print sciezka_source + nr_source
        os.remove( sciezka_source + nr_source)

