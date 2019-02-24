# -*- coding: utf-8 -*-

"""
@package ueda_reina_livertine_age_crawler.py
@brief 
@author stfate
"""

import scrapy
import requests
import os
import time


class UedaReinaLivertineAgeCrawlSpider(scrapy.Spider):
    name = "ueda-reina-livertine-age-crawl"
    ROOT_URL = "https://livertineage.jp/SHOP"
    download_root = "../../data/"
    
    def start_requests(self):
        urls = [
            f"{self.ROOT_URL}/2191100005.html",
            f"{self.ROOT_URL}/2191100006.html",
            f"{self.ROOT_URL}/2191100007.html"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        img_list = response.css("div.description img")
        for img in img_list:
            img_src = img.css("::attr(src)").extract_first()
            img_save_dir = os.path.join(self.download_root)
            url_bname = os.path.splitext(os.path.basename(response.url))[0]
            if img_src.find(url_bname) >= 0:
                if not os.path.exists(img_save_dir):
                    os.makedirs(img_save_dir)
                img_save_fn = os.path.join(img_save_dir, os.path.basename(img_src))
                with open(img_save_fn, "wb") as fo:
                    img_response = requests.get(img_src, stream=True)

                    if not img_response.ok:
                        print(img_response)

                    for block in img_response.iter_content(1024):
                        if not block:
                            break

                        fo.write(block)

                time.sleep(1.0)

                yield {"url": img_src}
