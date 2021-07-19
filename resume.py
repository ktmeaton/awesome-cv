#!/usr/bin/env python3

import os
import importlib

cwd = os.getcwd()

metadata_dir = os.path.join(cwd, "metadata")
template_dir = os.path.join(cwd, "templates")

sections = [
    "education"
]


for section in sections:
    template = importlib.import_module("templates." + section)
    metadata_path = os.path.join(metadata_dir, section + ".tsv")

    with open(metadata_path) as infile:
        metadata = [line.strip().split("\t") for line in infile.read().split("\n")]
        header = metadata[0]
        metadata = metadata[1:]

        # Check for newline problems
        if metadata[-1] == ['']:
            metadata = metadata[:-1]


    print(template.HEADER)
    for entry in metadata:
        data_dict = {column:value for column,value in zip(header, entry)}
        entry_tex = template.TEMPLATE.format(**data_dict)
        print(entry_tex)    
    print(template.FOOTER)
