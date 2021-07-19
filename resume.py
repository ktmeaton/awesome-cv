#!/usr/bin/env python3

import os
import importlib

cwd = os.getcwd()

metadata_dir = os.path.join(cwd, "metadata")
template_dir = os.path.join(cwd, "templates")

sections = [
    "summary",
    "education",
    "experience",
]


for section in sections:
    print(section)
    template = importlib.import_module("templates." + section)
    metadata_path = os.path.join(metadata_dir, section + ".tsv")
    out_path = os.path.join("resume", section + ".tex")

    with open(metadata_path) as infile:
        metadata = [line.strip().split("\t") for line in infile.read().split("\n")]
        header = metadata[0]
        metadata = metadata[1:]
        # Check for newline problems
        if metadata[-1] == ['']:
            metadata = metadata[:-1]

        # Format bullets
        if "bullets" in header:
            for entry in metadata:
                bullets_raw = entry[header.index("bullets")]
                bullets_split = bullets_raw.split(";")
                bullets_str = ["\item {" + val + "}" for val in bullets_split]
                bullets = "\n\t\t\t".join(bullets_str)

                entry[header.index("bullets")] = bullets

    # Write to the output resume directory
    with open(out_path, "w") as outfile:
        outfile.write(template.HEADER + "\n")
        for entry in metadata:
            data_dict = {column:value for column,value in zip(header, entry)}
            entry_tex = template.TEMPLATE.format(**data_dict)
            outfile.write(entry_tex + "\n")    
        outfile.write(template.FOOTER + "\n")
