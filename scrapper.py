#!/usr/bin/python
# -*- coding: utf-8 -*-

from splinter import Browser
import time
import re
import sys

#Definir o encoding por omissão como o UTF-8 devido a nomes com acentos
reload(sys)
sys.setdefaultencoding("utf-8")

if len(sys.argv) > 1:
    #Nome do professor a procurar
    nome = sys.argv[1]

    with Browser() as browser:
        browser.windows
        # Visit URL
        url = "http://rh.ufp.pt"
        browser.visit(url)
        browser.fill('Nome', nome.decode("utf-8"))
        # Find and click the 'search' button
        button = browser.find_by_xpath('//input[@type=\'image\']')
        # Interact with elements
        button.click()
        time.sleep(1)
        URL = re.findall(r"(rh/Detalhe/.{3})", browser.html)
        if len(URL) > 1:
            for match in URL:
                print re.sub(r"rh/Detalhe/", "", match)
        elif len(URL) == 1:
            print re.sub(r"rh/Detalhe/", "", URL[0])
        else:
            print "Não encontrado"
else:
    print "Erro! Argumento em falta. Uso: python scrapper.py \"nomeDoProfessor\""