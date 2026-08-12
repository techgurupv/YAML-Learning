import yaml

with open("enterprise_rag.yaml", "r") as file:
    config = yaml.safe_load(file)
print(config)

# So YAML isn't directly accessed by Python.

# Instead:
# YAML
#  ↓
# PyYAML
#  ↓
# Python objects

# yaml.safe_load(file) reads a YAML file or stream and converts its content into equivalent Python data structures (such as dictionaries, lists, strings, numbers, and booleans).

# It is designed to safely parse untrusted input by restricting the data types to standard Python primitives, preventing the execution of arbitrary code during parsing.

# Key Characteristics
# Security (safe_load vs load): Standard yaml.load() can construct arbitrary Python objects using YAML tags (e.g., !!python/object/apply), which exposes your application to Remote Code Execution (RCE) attacks if the YAML comes from an untrusted source. yaml.safe_load() disables these dynamic object constructors.

# Stream Input: Accepts either an open file object (e.g., open('config.yaml')) or a plain string containing valid YAML data.

# Error Handling: Raises yaml.YAMLError (specifically yaml.scanner.ScannerError or yaml.parser.ParserError) if the file contains invalid syntax.

# How It Translates YAML to Python
# YAML Data Type,Python Data Type,Example YAML,Example Python Output
# Key-value pair,dict,server: localhost,{'server': 'localhost'}
# List,list,- apple\n- banana,"['apple', 'banana']"
# Number,int or float,port: 8080,{'port': 8080}
# Boolean,bool,debug: true,{'debug': True}
# Empty file,NoneType,(empty),None