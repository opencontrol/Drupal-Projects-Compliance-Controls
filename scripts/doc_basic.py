#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Script for generating basic document

Usage:
# Run from repository root directory
python ./scripts/doc_basic.py

"""

__author__ = "Greg Elin (gregelin@govready.com)"
__version__ = "$Revision: 0.2.1 $"
__date__ = "$Date: 2017/06/05 15:35:00 $"
__copyright__ = "Copyright (c) 2017 GovReady PBC"
__license__ = "Apache Software License 2.0"

import os
import yaml
import compliancelib
import jinja2

# Settings
dir_path         = os.path.dirname(os.path.realpath(__file__))
print('dir_path', dir_path)
opencontrol_repo = 'https://github.com/opencontrol/Drupal-Projects-Compliance-Controls'
opencontrol_file = '../opencontrol.yaml'
output_file      = dir_path+'/../docs/BASIC.md'
print('output_file', output_file)
controllist      = ["AC-2","AC-6","AC-6 (1)", "AC-12", "SC-5", "SI-7"]
# controllist    = ["AC-2","AC-6","AC-6 (1)", "AC-12", "AU-2", "AU-3", "AU-7", "AU-8", "AU-9", "AU-14", "SC-5", "SI-7"]

# Load jina environment to get templates
templateLoader = jinja2.FileSystemLoader( searchpath=dir_path )
templateEnv    = jinja2.Environment( loader=templateLoader )
TEMPLATE_FILE  = "templates/BASIC.md"
template       = templateEnv.get_template( TEMPLATE_FILE )

# Create system compliance instance and load OpenControl repo
sp = compliancelib.SystemCompliance()
print("Loading OpenControl repository: {}".format(opencontrol_repo))
sp.load_system_from_opencontrol_repo(opencontrol_repo)

# Figure out all the controls that are supported by the repo
# TODO

# Prepare content for BASIC.md template
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
# 
#print(controls)
output_text = template.render( {"controls": controls} )
with open(output_file, "w") as f:
    f.write(output_text)
print("File written: {}".format(output_file))

