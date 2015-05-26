__author__ = 'Graham'
import Test
from Bio import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO

infile = list(SeqIO.parse('rosalind_grph.txt', 'fasta'))
list_edges = []
for fragment in infile:
    for other_fragment in infile:
        if fragment.seq[-3:] == other_fragment.seq[0:3] and fragment != other_fragment:
            list_edges.append(str(fragment.id + ' ' + other_fragment.id))

for entry in list_edges:
        print entry

