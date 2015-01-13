import urllib2
import csv
#from lxml import etree
#from xml.etree import ElementTree as etree
from bs4 import BeautifulSoup

__author__ = 'adenton'

def getSRAofTXID(txid):
    strbefore = 'http://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?save=efetch&db=sra&rettype=runinfo&term=txid'
    response = urllib2.urlopen(strbefore + txid)
#    lines = response.readlines()
    lines = csv.reader(response)
    bases=0
    for row in lines:
        try:
            bases += int(row[4])
        except:
            if not row[4] == 'bases':
                print 'do you have the right column?' + str(row[4])
    return(bases)

def getChildrenTXID(txid):
    strbefore = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?db=taxonomy&dbfrom=taxonomy&id='
    response = urllib2.urlopen(strbefore + txid)
    treestring = response.read()
    tree = BeautifulSoup(treestring)
    print strbefore+txid
#    for child in tree:

    print tree
#    pass

soffi = '38868'
rosmarinus = '39177'
Lamiaceae = '4136'
x = getChildrenTXID(Lamiaceae)


#x = getSRAofTXID(soffi)
#y = getSRAofTXID(rosmarinus)

#print str(x) +', ' + str(y)
#download meta data from SRA
#e.g.
# wget -O  'http://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?save=efetch&db=sra&rettype=runinfo&term='
# http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=sra&term=txid39367&retmax=30
#http://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?db=taxonomy&dbfrom=taxonomy&id=4143