# Description: Yaml file read / parse out HCL map
# Author: Corne Bester
# Date : Oct 2018
# tags: tags python python3 yaml dict HCL terraform
# references / sources:

import yaml
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, default='sample.yml')
parser.add_argument('--output', type=str, default='sample.auto.tfvars')
args = parser.parse_args()

cwd = Path.cwd()  # get current working dir

MyDict = yaml.load(open(str(args.input)))


n = int
n = 0    
with open(args.output, "w",encoding='utf-8') as file_handler:
    #file_handler.writelines('variable "whitelist" {\n')
    #file_handler.writelines('\t' + 'type = "map"\n')
    file_handler.writelines('whitelist = {\n')
    for key, value in MyDict.items():
        n += 1
        file_handler.writelines(str("\t" + '"{0}"'.format(key) + " = " + '"{0}"'.format(value) + "\n"))
        if len(MyDict) == n:
            pass
            #file_handler.writelines('\t' + '}\n')
            file_handler.writelines('}\n')
print("Wrote: ", args.output )
print("From input file: ", args.input)