__author__ = 'Graham'
import sys
sys.path.append('/Users/Graham/Desktop/biopython')
from Bio import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO
from Bio.Data import IUPACData
import Genome_Assembly1

happy = ['Heloo', 'He']
unhappy = []

inlist = list(SeqIO.parse('rosalind_long.txt', 'fasta'))
print Genome_Assembly1.assemble_genome(inlist)



