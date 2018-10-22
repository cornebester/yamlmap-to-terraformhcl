# Description: Yaml file read / parse out HCL map
# Author: Corne Bester
# Date : 23 May 2018
# tags: tags python python3 yaml dict HCL terraform
# references / sources:

'''
tf file format

'variable "cidrs" {'
'  type = "map"'
'default = {'
    "us-east-1" = "ami-b374d5a5"
    "us-west-2" = "ami-4b32be2b"
'  }'
'}'

tfvars file map format 

'whitelist = {'
    "us-east-1" = "ami-b374d5a5"
    "us-west-2" = "ami-4b32be2b"
'  }'


'''
import yaml

MyDict = yaml.load(open(r"C:\Users\cbester\Dropbox\devops\StatPro\infrastructure\whitelist_trusted_ips.yaml"))
# r = raw string else have to use double backslashes to escape path \\

n = int
n = 0    
with open('c:\\scratch\\whitelist_varmap.auto.tfvars', "w",encoding='utf-8') as file_handler:
    #file_handler.writelines('variable "whitelist" {\n')
    #file_handler.writelines('\t' + 'type = "map"\n')
    file_handler.writelines('\t' + 'whitelist = {\n')
    for key, value in MyDict.items():
        n += 1
        file_handler.writelines(str("\t\t" + '"{0}"'.format(key) + " = " + '"{0}"'.format(value) + "\n"))
        if len(MyDict) == n:
            pass
            #file_handler.writelines('\t' + '}\n')
            file_handler.writelines('}')
