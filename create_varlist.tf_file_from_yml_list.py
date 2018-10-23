# Description: Yaml file read / parse output HCL variable list
# Author: Corne Bester
# Date : Oct 2018
# tags: tags python python3 yaml dict HCL terraform
# references / sources:

import yaml
import json
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, default='sample.yml')
parser.add_argument('--output', type=str, default='sample.tf')
args = parser.parse_args()

cwd = Path.cwd()  # get current working dir

MyDict = yaml.load(open(str(args.input)))

WhiteList = list(MyDict.values())

with open(args.output, "w", encoding='utf-8') as file_handler:
    file_handler.writelines('variable "whitelist-list" {\n')
    file_handler.writelines('  ' + 'type\t= "list"\n')
    file_handler.writelines('  ' + 'default = ')
    file_handler.writelines(json.dumps(WhiteList)+'\n')
    file_handler.writelines('}'+'\n')
print("Wrote: ", args.output)
print("From input file: ", args.input)
