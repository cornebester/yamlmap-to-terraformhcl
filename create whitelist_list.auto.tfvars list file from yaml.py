# Description: Yaml file read / parse
# Author: Corne Bester
# Date : 23 May 2018
# tags: tags python python3 yaml dict terraform
# references / sources:

import yaml
import json

MyDict = yaml.load(open(r"C:\Users\cbester\Dropbox\devops\StatPro\infrastructure\whitelist_trusted_ips.yaml"))
# r = raw string else have to use double backslashes to escape path \\
whitelist = []
n = int
del whitelist[:]
n = 0

for k, v in MyDict.items():
    whitelist.append(v)
    n += 1
    if len(MyDict) == n:
        pass
        dump = json.dumps(whitelist)
        createfile = 'whitelist = ' + str(dump)
        with open('c:\\scratch\\whitelist_list.auto.tfvars', "w",encoding='utf-8') as file_handler:
            file_handler.write(createfile)






