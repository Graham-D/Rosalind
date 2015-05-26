__author__ = 'Graham'

import sys
import math
sys.path.append('/Users/Graham/Desktop/Personal/Python Projects/biopython')
from Bio.Data import IUPACData
from Bio.Seq import Seq


def find_restriction_sites(indna):
    sites = {}
    i = 0
    while i < len(indna):
        if indna[i:i+12] == indna[i:i+12].reverse_complement() and i < len(indna) - 11:
            sites[i+1] = 12
        elif indna[i:i+10] == indna[i:i+10].reverse_complement() and i < len(indna) - 9:
            sites[i+1] = 10
        elif indna[i:i+8] == indna[i:i+8].reverse_complement() and i < len(indna) - 7:
            sites[i+1] = 8
        elif indna[i:i+6] == indna[i:i+6].reverse_complement() and i < len(indna) - 5:
            sites[i+1] = 6
        elif indna[i:i+4] == indna[i:i+4].reverse_complement() and i < len(indna) - 3:
            sites[i+1] = 4
        i += 1
    return sites


def calc_prot_mass(inprot):
    mass = 0
    for peptide in inprot:
        mass += IUPACData.monoisotopic_protein_weights[peptide] - 18.01056
    return mass


def find_orf(insequence):
    list_orfs = []
    stops = ['TAA', 'TAG', 'TGA']
    i = 0
    while i < len(insequence)-2:
        if insequence[i:i+3] == 'ATG':
            j = i + 3
            while j < len(insequence)-2:
                if insequence[j:j+3] in stops:
                    list_orfs.append(insequence[i:j])
                    break
                j += 3
        i += 1
    return list_orfs


def splice_introns(in_dna,in_introns):
    spliced_dna = in_dna
    for intron in in_introns:
        spliced_dna = spliced_dna[0:spliced_dna.find(intron.seq)]\
                      + spliced_dna[spliced_dna.find(intron.seq)+len(intron.seq):]
    return spliced_dna


def fib(num_months, lifespan):
    new_rabbit_pairs = 1
    old_rabbit_pairs = 0
    for month in range(num_months-1):
        temp = new_rabbit_pairs
        new_rabbit_pairs = old_rabbit_pairs * 2
        old_rabbit_pairs += temp
    total = old_rabbit_pairs + new_rabbit_pairs
    print total


def find_consensus(inlist):
    list_of_nucs = []
    consensus = ''
    for num in range(len(inlist[0])):
        list_of_nucs.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})
    for sequence in inlist:
        for num in range(len(sequence)):
            list_of_nucs[num][sequence[num]] += 1
    for index in list_of_nucs:
        max_num = 0
        for key in index:
            if index[key] > max_num:
                max_num = index[key]
                con = key
        consensus += con
    print consensus
    for key in list_of_nucs[0]:
        print key + ':',
        i = 0
        while i < len(list_of_nucs):
            if i == len(list_of_nucs)-1:
                print str(list_of_nucs[i][key])
            else:
                print str(list_of_nucs[i][key]),
            i += 1


def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
