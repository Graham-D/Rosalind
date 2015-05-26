__author__ = 'Graham'


def assemble_genome(list_reads):
    genome = list_reads[0].seq
    list_reads.remove(list_reads[0])
    j = 0
    while j < range(len(list_reads)+1) and list_reads:
        for read in list_reads:
            if read.seq in genome:
                break
            i = len(read.seq)
            while list_reads and i >= (len(read.seq)/2):
                if read.seq[:i] in genome and read.seq[:i+1] not in genome:
                    genome += read.seq[i:]
                    list_reads.remove(read)
                    j+=1
                    break
                elif read.seq[-i:] in genome and read.seq[-(i+1):] not in genome:
                    genome = read.seq[:-i] + genome
                    list_reads.remove(read)
                    j+=1
                    break
                i -= 1
    return genome