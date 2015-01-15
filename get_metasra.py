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

def idsFromXML(xml):
    bs = BeautifulSoup(xml)
    bsids = bs.find_all('id')
    idstrings = [x.getText() for x in bsids]
    return (idstrings)


def getPUBMEDids(q1,q2,retmax=1000000):
    strbefore = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&usehistory=y&retmax='+str(retmax)+'&term='
    response1 = urllib2.urlopen(strbefore + q1)
    response2 = urllib2.urlopen(strbefore + q2)
    ids1 =  idsFromXML(response1.read())
    ids2 = idsFromXML(response2.read())
    intersect = set(ids2) & set(ids1)
    l1 = len(ids1)
    lint = len(intersect)
    out = float(lint)/float(l1)
    return (out)



soffi = '38868'
rosmarinus = '39177'
Lamiaceae = '4136'
#x = getChildrenTXID(Lamiaceae)
test = open('testncbi.xml').read()
#idsFromXML(test)
x = getPUBMEDids(q1='Camphor',q2='Salvia+officinalis')
print x
#x = getSRAofTXID(soffi)
#y = getSRAofTXID(rosmarinus)

#print str(x) +', ' + str(y)
#download meta data from SRA
#e.g.
# wget -O  'http://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?save=efetch&db=sra&rettype=runinfo&term='
# http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=sra&term=txid39367&retmax=30
#http://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?db=taxonomy&dbfrom=taxonomy&id=4143


#example with history
#http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&usehistory=y&retmax=10&term=Salvia
#webenv out of first xml
#http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&rettype=abstract&id=25582415,25577438&webenv=NCID_1_397854919_130.14.18.34_9001_1421356317_1882704335_0MetA0_S_MegaStore_F_1