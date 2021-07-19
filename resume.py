#!/usr/bin/env python3

import os
import importlib

cwd = os.getcwd()

metadata_dir = os.path.join(cwd, "metadata")
template_dir = os.path.join(cwd, "templates")

sections = {
    "summary" : 1,
    "education" : 5,
    "experience": 7,
    "output": 3,
}


for section in sections:
    template = importlib.import_module("templates." + section)
    metadata_path = os.path.join(metadata_dir, section + ".tsv")
    out_path = os.path.join("resume", section + ".tex")
    num_entries = sections[section]

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

        # Special sections that have sub-categories as type
        if "category" in header:
            cat_i = header.index("category")
            categories_list = [t[cat_i] for t in metadata]

            # Remove duplicates and preserve order
            categories = []
            for cat in categories_list:
                if cat not in categories:
                    categories.append(cat)

            for category in categories:
                outfile.write(template.SUB_HEADER.format(category=category) + "\n")
                entry_i = 0
                for entry in metadata:
                    if entry[cat_i] != category: continue
                    entry_i += 1
                    if entry_i > num_entries: break
                    data_dict = {column:value for column,value in zip(header, entry)}
                    entry_tex = template.TEMPLATE.format(**data_dict)
                    outfile.write(entry_tex + "\n")   

                outfile.write(template.SUB_FOOTER + "\n")

        else:
            # Normal
            entry_i = 0
            for entry in metadata:
                entry_i += 1   
                if entry_i > num_entries: break             
                data_dict = {column:value for column,value in zip(header, entry)}
                entry_tex = template.TEMPLATE.format(**data_dict)
                outfile.write(entry_tex + "\n")   

        outfile.write(template.FOOTER + "\n")
