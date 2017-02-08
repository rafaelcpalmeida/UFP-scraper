#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from bs4 import BeautifulSoup
import requests
import re

#Definir o encoding por omissão como o UTF-8 devido a nomes com acentos
reload(sys)
sys.setdefaultencoding("utf-8")

if len(sys.argv) > 1:
    url = 'http://rh.ufp.pt/rh/Detalhe/'+sys.argv[1]
    r  = requests.get(url)
    
    data = r.text
    soup = BeautifulSoup(data, "lxml")

    nome = soup.find("b")

    print nome.contents[0].encode("utf-8")
    print ""
    
    for lists in soup.find_all("ul"):
        print lists.previous_element
        for content in lists.contents:
            print content.contents[0].encode("utf-8")
        print ""
    for element in soup.find_all('p'):
        if re.search(r"Última", str(element)):
            print element.contents[0]
            print ""
        
        if re.search(r"Correio", str(element)):
            print element.contents[0]
else:
    print "Erro! Argumento em falta. Uso: python spider.py \"aliasDoProfessor\""