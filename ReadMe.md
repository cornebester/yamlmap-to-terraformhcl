# Terraform variable files creation from yml map

Python3 scripts that read a single map from simple yaml/yml file and output values as terraform list(values) or a key value pair map variables

My initial use case is to read form a globally maintained whitelisted/labeled yaml file and output to terraform variables for comsumption by AWS/Azure security groups

## Scripts

CLI arguments is optional, using the sample files in root if no arguments specified

    script --i (input) and --o (output)

### Yaml file read, parse and output HCL syntax variable list as .tf file
    python create_varlist.tf_file_from_yml_list.py --i src_path_file --o dest_path_file
### Yaml file read, parse and output HCL syntax variable list as .auto.tfvars file
    python create_varlist.auto.tfvars_file_from_yml_list.py --i src_path_file --o dest_path_file

### Yaml file read, parse and output HCL syntax variable map as .tf
    python create_varmap.tf_file_from_yml_list.py --i src_path_file --o dest_path_file
### Yaml file read, parse, output HCL syntax variable map as .auto.tfvars
    python create_varmap.auto.tfvars_file_from_yml_list.py --i src_path_file --o dest_path_file

Optionally run _terraform fmt_ in destination path to correct spacing, check syntax

## Dependencies

### Windows
    python -m pip install --trusted-host pypi.python.org -r requirements.txt

### Debian
    python3 -m pip install --trusted-host pypi.python.org -r requirements.txt

## References

HCL (HashiCorp Configuration Language)  
<https://github.com/hashicorp/hcl/blob/master/README.md#syntax>
<https://www.terraform.io/docs/configuration/variables.html>



