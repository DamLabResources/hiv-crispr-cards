import pandas as pd
import csv
from Bio.Seq import reverse_complement


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






