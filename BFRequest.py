# @Author: Gao Bo
# @Date:   2016-10-29T19:53:25-04:00
# @Last modified by:   Gao Bo
# @Last modified time: 2016-10-30T12:11:43-04:00



import json
import requests
from collections import OrderedDict
import sys

urlprefix = 'https://www.buzzfeed.com/api/v2/feeds/'


def getBFTrends(sectionName, maxN=20, dumpHuman=False):
    '''
    parameters:
    sectionName     the name of the section you want
    maxN            the max number of trends you want
    dumpHuman       whether to dump the buzzfeed to a human readable file
    '''

    BFTrends = requests.get(urlprefix+sectionName).json(object_pairs_hook=OrderedDict)

    if dumpHuman:
        outfile = open('bfTrendsOutput.txt', 'w')
        outfile.write(json.dumps(BFTrends, sort_keys=True, indent=4, separators=(',', ': ')))
        outfile.close()

    parsedBFTrends = []
    buzzesList = BFTrends['buzzes']
    for buzz in buzzesList:
        tbuzz = {}
        tbuzz['title'] = buzz['title']
        tbuzz['category'] = buzz['category']
        tbuzz['id'] = buzz['id']
        tbuzz['published_date'] = buzz['published_date']
        tbuzz['tags'] = buzz['tags']
        parsedBFTrends.append(tbuzz)
        if len(parsedBFTrends) >= maxN: break

    return parsedBFTrends

if __name__ == '__main__':
    argc = len(sys.argv)
    # print(argc)
    if argc == 1 or argc > 3:
        print ('''
        Usage:
        python BFRequest.py [sectionNum, maxN]
        ''')
        parsedBFTrends = getBFTrends('trending')
        # parsedBFTrends = getBFTrends('life')
    elif argc == 2:
        parsedBFTrends = getBFTrends(sys.argv[1])
    elif argc == 3:
        parsedBFTrends = getBFTrends(sys.argv[1], int(sys.argv[2]))

    for buzz in parsedBFTrends:
        print(buzz['title'])
