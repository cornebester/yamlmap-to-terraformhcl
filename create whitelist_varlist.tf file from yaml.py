# Description: Yaml file read / parse out HCL map
# Author: Corne Bester
# Date : 23 May 2018
# tags: tags python python3 yaml dict HCL terraform
# references / sources:

import yaml
import json

MyDict = yaml.load(open(
    r"C:\Users\cbester\Dropbox\devops\StatPro\infrastructure\whitelist_trusted_ips.yaml"))
# r = raw string else have to use double backslashes to escape path \\
WhiteList = list(MyDict.values())


with open('c:\\scratch\\whitelist_varlist.tf', "w", encoding='utf-8') as file_handler:
    file_handler.writelines('variable "whitelist-list" {\n')
    file_handler.writelines('  ' + 'type\t\t= "list"\n')
    file_handler.writelines('  ' + 'default = ')
    file_handler.writelines(json.dumps(WhiteList)+'\n')
    file_handler.writelines('}'+'\n')
