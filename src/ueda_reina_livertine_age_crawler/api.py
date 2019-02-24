#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@package api.py
@brief
@author stfate
"""

import subprocess
import os
import json


CRAWLER_DIR = os.path.dirname( os.path.abspath(__file__) )

def download_images():
    cur_dir = os.getcwd()
    os.chdir(CRAWLER_DIR)

    cmd = [
        "scrapy", "crawl", "ueda-reina-livertine-age-crawl",
        "-t", "json",
        "-o", "-"
    ]
    output_str = subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode("utf-8")
    print("output_str=", output_str)
    output_dict = json.loads(output_str)
    os.chdir(cur_dir)

    return output_dict
