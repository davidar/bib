import sys
from subprocess import Popen, PIPE
from collections import OrderedDict
import re
import time
import random
from xml.etree import ElementTree
from urlparse import urlparse
from kitchen.text.converters import getwriter

import pybtex.core
import pybtex.database.input.bibtex
import pybtex.database.output.bibtex

from unicode_to_latex import unicode_to_latex

# why is utf8 not default already?
reload(sys); sys.setdefaultencoding('utf8')
UTF8Writer = getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

# make bibtex fields ordered
class FieldDict(OrderedDict):
    def __init__(self, parent, *args, **kwargw):
        self.parent = parent
        OrderedDict.__init__(self, *args, **kwargw)
    def __missing__(self, key):
        if key in self.parent.persons:
            persons = self.parent.persons[key]
            return ' and '.join(unicode(person) for person in persons)
        elif 'crossref' in self:
            return self.parent.get_crossref().fields[key]
        else:
            raise KeyError(key)
pybtex.core.FieldDict = FieldDict
pybtex.database.FieldDict = FieldDict

class BibWriter(pybtex.database.output.bibtex.Writer):
    def quote(self, s):
        self.check_braces(s)
        #if type(s) is str: s = s.decode('utf8')
        return u'{%s}' % s

def parse_bib(f=sys.stdin):
    parser = pybtex.database.input.bibtex.Parser('utf8')
    parser.data.entries = OrderedDict()
    return parser.parse_stream(f)

def write_bib(bib, f=sys.stdout):
    writer = BibWriter()
    writer.write_stream(bib, f)

def resolve_bib(uri):
    p = Popen(['./bib-resolve', uri], stdout=PIPE)
    return parse_bib(p.stdout)

def resolve_url(uri):
    p = Popen(['./bib-resolve', uri, 'url'], stdout=PIPE)
    for line in p.stdout: yield line.strip()

def dl_pdf(url):
    p = Popen(['./bib-dl', url], stdout=PIPE)
    return p.stdout.read().strip()

def bib_search(service, s):
    p = Popen(['./bib-search-' + service, s], stdout=PIPE)
    for line in p.stdout: yield line.split('\t')

def merge_dict(d1, d2={}, **kwargs):
    for k,v in d2.items():
        if k not in d1 and v: d1[k] = v
    if kwargs: merge_dict(d1, kwargs)

def parse_xml_flat(f=sys.stdin):
    try:
        tree = ElementTree.parse(f)
        root = tree.getroot()
        for e in root:
            yield e.tag, e.attrib, e.text
    except ElementTree.ParseError:
        pass

def isurl(s):
    o = urlparse(s)
    return (o.scheme in ('http','https','ftp'))

u2table = {}
for k,v in unicode_to_latex.iteritems():
    if len(k) == 1:
        u2table[ord(k)] = unicode(v.replace(' ','{}'))
def u2latex(s):
    return s.translate(u2table)

def str_norm(s):
    s = re.sub(r'\W+', ' ', s).lower().strip()
    return ' '.join(s.split())

def streq_norm(s1,s2):
    return str_norm(s1) == str_norm(s2)

def random_sleep(a=0.5, b=1.5):
    time.sleep(random.uniform(a,b))
