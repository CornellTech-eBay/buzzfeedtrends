# @Author: Gao Bo
# @Date:   2016-10-29T19:53:25-04:00
# @Last modified by:   Gao Bo
# @Last modified time: 2016-10-29T20:22:35-04:00



import json
import requests

urlprefix = 'https://www.buzzfeed.com/api/v2/feeds/'


def getBFTrends(sectionName, maxN=20):

    bftrends = requests.get(urlprefix+sectionName).json()



    outfile = open('bfTrendsOutput.txt', 'w')
    outfile.write(json.dumps(bftrends, sort_keys=True, indent=4, separators=(',', ': ')))
    outfile.close()

if __name__ == '__main__':
    bztrendsList = getBFTrends('trending')
