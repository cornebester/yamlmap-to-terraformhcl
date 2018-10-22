# Description: Yaml file read / parse out HCL map
# Author: Corne Bester
# Date : 23 May 2018
# tags: tags python python3 yaml dict HCL terraform
# references / sources:

import yaml

MyDict = yaml.load(open(r"C:\Users\cbester\Dropbox\devops\StatPro\infrastructure\whitelist_trusted_ips.yaml"))
# r = raw string else have to use double backslashes to escape path \\

n = int
n = 0    
with open('c:\\scratch\\whitelist_varmap.tf', "w",encoding='utf-8') as file_handler:
    file_handler.writelines('variable "whitelist" {\n')
    file_handler.writelines('  ' + 'type = "map"\n')
    file_handler.writelines('\n')
    file_handler.writelines('  ' + 'default = {\n')
    for key, value in MyDict.items():
        n += 1
        file_handler.writelines('\t{:<18} {:<1} "{}"\n'.format('"{}"'.format(key), "=", value))
        if len(MyDict) == n:
            pass
            file_handler.writelines('  ' + '}\n')
            file_handler.writelines('}\n')
