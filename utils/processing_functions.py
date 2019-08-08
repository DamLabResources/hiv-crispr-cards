import pandas as pd
import csv
from Bio.Seq import reverse_complement
from Bio import Entrez
import xml.etree.ElementTree as ET

Entrez.email = "wnd22@drexel.edu"


def process_pmid(pmid):

    handle = Entrez.efetch(db="pubmed",
                           id=str(pmid),
                           rettype="xml")
    tree = ET.parse(handle)
    root = tree.getroot()

    pub_info = {}

    pub_info['pub_date'] = {}
    try:
        comp = next(root.iter('DateCompleted'))
        for dt in comp:
            pub_info['pub_date'][dt.tag] = int(dt.text)
    except StopIteration:
        print('Missing dates for PMID:%i' % pmid)

    journal = next(root.iter('Journal'))
    try:
        pub_info['Journal'] = next(journal.iter('Title')).text
        pub_info['Title'] = next(root.iter('ArticleTitle')).text
        pub_info['Abstract'] = next(root.iter('AbstractText')).text
    except StopIteration:
        print('Missing title info for PMID:%i' % pmid)

    pub_info['AuthorList'] = []

    try:
        authors = next(root.iter('AuthorList'))
    except StopIteration:
        print('Missing author for list PMID:%i' % pmid)
        authors = None

    if authors is not None:
        for author in authors.iter('Author'):
            pub_info['AuthorList'].append({})
            for nm in author:
                if nm.tag != 'AffiliationInfo':
                    pub_info['AuthorList'][-1][nm.tag] = nm.text

    return pub_info


def normalize_grna(inp):
    parts = inp.split('.')
    try:
        if len(parts[0]) > len(parts[1]):
            return parts[0], '+'
        else:
            return reverse_complement(parts[1]), '-'
    except IndexError:
        return inp, '+'


def make_gff_from_extraannot(in_path, out_path):
    """Makes GFF file from the currently formatted gRNA list.
    """

    data = pd.read_excel(in_path).dropna(subset = ['Start']).sort_values(by = ['Start'])

    fields = ['chrom', 'source', 'type',
              'start', 'end',
              'score', 'strand',
              'phase', 'attrs']

    with open(out_path, 'w') as handle:

        writer = csv.DictWriter(handle, fields, delimiter = '\t')

        for _, row in data.iterrows():
            info = {'chrom':'K03455.1',
                    'source': '.',
                    'start': int(row['Start']),
                    'end': int(row['Stop'])}

            spacer, strand = normalize_grna(row['gRNA'])
            info['strand'] = strand

            attrs = ';'.join(['Name='+str(row['Name']),
                              'PMID=%i' % row['Citation'],
                              'protspacer=' + spacer])
            info['attrs'] = attrs

            writer.writerow(info)






