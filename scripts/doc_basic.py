#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Script for generating basic document

Usage:
python3 doc_basic.py


"""

__author__ = "Greg Elin (gregelin@govready.com)"
__version__ = "$Revision: 0.1.0 $"
__date__ = "$Date: 2017/06/03 21:35:00 $"
__copyright__ = "Copyright (c) 2017 GovReady PBC"
__license__ = "Apache Software License 2.0"

import os
import yaml
import compliancelib
import jinja2



# Settings
opencontrol_repo = 'https://github.com/opencontrol/Drupal-Plugins-Compliance-Controls'
opencontrol_file = '../opencontrol.yaml'
output_file      = '../docs/BASIC.md'
controllist      = ["AC-2","AC-6","AC-6 (1)", "AC-12", "SC-5", "SI-7"]
# controllist    = ["AC-2","AC-6","AC-6 (1)", "AC-12", "AU-2", "AU-3", "AU-7", "AU-8", "AU-9", "AU-14", "SC-5", "SI-7"]

# Load jina environment to get templates
templateLoader = jinja2.FileSystemLoader( searchpath="./" )
templateEnv    = jinja2.Environment( loader=templateLoader )
TEMPLATE_FILE  = "templates/BASIC.md"
template       = templateEnv.get_template( TEMPLATE_FILE )

# Create system compliance instance
sp = compliancelib.SystemCompliance()
# Load OpenControl repo
sp.load_system_from_opencontrol_repo(opencontrol_repo)

# Figure out all the controls that are supported by the repo
# TODO

# Loop through supported controls and capture basic description document
# content = ""
# for c in controllist:
#     if c is None:
#         continue
#     content += "## {} {} \n\n".format(sp.control(c).id, sp.control(c).title)
#     for component in sp.control(c).components_dict.keys():
#         content += "{}".format(sp.control(c).components_dict[component][0]['narrative'][0]['text'].replace("\n"," "))
#         content += "\n\n"

# print("\n\n PRINTING OUTPUT \n")
# print(content)

# with open(output_file, "w") as f:
#     f.write(content)
# print("File written: ", output_file)

# Now, with a template!

controls = {}
for c in controllist:
    texts = []
    for component in sp.control(c).components_dict.keys():
        texts.append("{}".format(sp.control(c).components_dict[component][0]['narrative'][0]['text'].replace("\n"," ")))

    controls[c] = { 
        "id": sp.control(c).id, 
        "title": sp.control(c).title, 
        "texts": texts,
    }

# print("\n\n PRINTING OUTPUT \n")
#print(controls)

output_text = template.render( {"controls": controls} )
with open(output_file, "w") as f:
    f.write(output_text)
print("File written: ", output_file)

