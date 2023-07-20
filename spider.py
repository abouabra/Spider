import requests
from bs4 import BeautifulSoup
import sys

"""
/spider [-rlp] URL
• Option -r : recursively downloads the images in a URL received as a parameter.
• Option -r -l [N] : indicates the maximum depth level of the recursive download.
If not indicated, it will be 5.
• Option -p [PATH] : indicates the path where the downloaded files will be saved.
If not specified, ./data/ will be used.
"""
import argparse

parser = argparse.ArgumentParser(prog='Spider',description='The spider program allow you to extract all the images from a website, recursively, by providing a url as a parameter.')

parser.add_argument('-r', dest="recursively", action='store_true', help='recursively downloads the images in a URL received as a parameter.')

req_grp = parser.add_argument_group("require arguments")
req_grp.add_argument('-l', dest="limit",required=False, default=5, help='indicates the maximum depth level of the recursive download.')
req_grp.add_argument('-p', dest="path", required=False, help='indicates the path where the downloaded files will be saved.')

parser.add_argument('url', type=str, help='url to download')

args = parser.parse_args()
print(args.recursively, args.limit, args.path, args.url)