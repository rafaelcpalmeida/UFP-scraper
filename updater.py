#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import sys
import json
import os

#Definir o encoding por omissão como o UTF-8 devido a nomes com acentos
reload(sys)
sys.setdefaultencoding("utf-8")

apiURL = "http://ufp-api.dev/api/v1/"

print ""
print '+-----------------------------------+'
print "|  Updating Teachers information... |"
print '+-----------------------------------+'
print ""

r  = requests.get(apiURL + "teachers", params={'api_token': 1})

data = json.loads(r.text)

if(data["status"] == "Ok"):
    for detail in data["message"]:
        print detail["alias"]
        os.system("python teachers_updater.py " + detail["alias"])
else:
    print "Ocorreu um erro. Mensagem: " + data["message"]