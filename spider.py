#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from bs4 import BeautifulSoup
import requests
import re
import json

#Definir o encoding por omissão como o UTF-8 devido a nomes com acentos
reload(sys)
sys.setdefaultencoding("utf-8")

if len(sys.argv) > 1:
    details = {}
    url = 'http://rh.ufp.pt/rh/Detalhe/'+sys.argv[1]
    r  = requests.get(url)

    data = r.text
    soup = BeautifulSoup(data, "lxml")

    nome = soup.find("b")

    details["name"] = nome.contents[0].encode("utf-8")
    
    for lists in soup.find_all("ul"):
        details[lists.previous_element] = []
        for content in lists.contents:
            details[lists.previous_element].append(content.contents[0].encode("utf-8"))
    for element in soup.find_all('p'):
        if re.search(r"Última", str(element)):
            details["atualizacao"] = element.contents[0]
        
        if re.search(r"Correio", str(element)):
            details["contactos"] = element.contents[0]

    print json.dumps(details)
else:
    print "Erro! Argumento em falta. Uso: python spider.py \"aliasDoProfessor\""