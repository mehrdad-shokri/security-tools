#!/usr/bin/python
#
# Python script skeleton
#

# module imports
import requests
import sys

def main(url):
    if 'http://' not in url:
        url = 'http://' + url
    
    req = requests.get(url)
    print req.headers
    
if __name__ == '__main__':
    url = sys.argv[1]
    
    main(url)