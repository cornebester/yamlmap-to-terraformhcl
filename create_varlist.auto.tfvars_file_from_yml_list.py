# Description: Yaml file read / parse output terraform list variable as auto.tfvars
# Author: Corne Bester
# Date : Oct 2018
# tags: tags python python3 yaml dict terraform
# references / sources:

import yaml
import json
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, default='sample.yml')
parser.add_argument('--output', type=str, default='sample.auto.tfvars')
args = parser.parse_args()

cwd = Path.cwd()  # get current working dir

MyDict = yaml.load(open(str(args.input)))

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
        with open(args.output, "w",encoding='utf-8') as file_handler:
            file_handler.write(createfile)
print("Wrote: ", args.output )
print("From input file: ", args.input)





