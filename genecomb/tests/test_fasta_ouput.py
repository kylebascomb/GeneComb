from genecomb.genecomb import GeneComb
from genecomb.genecomb import read_fasta
import pytest


@pytest.mark.parametrize(
    "filepath, header, seq",
    [
        (
            "tests/fasta_output_files/homo_seq.fasta",
            ">PA369630.1 JP 2021531802-A/1: ANTIBODY BINDING TO HUMAN HER2 AND PREPARATION METHOD AND USE THEREOF",
            "ATGGAGCTGGCGGCCTTGTGCCGCTGGGGGCTCCTCCTCGCCCTCTTGCCCCCCGGAGCCGCGAGCACCCAAGTGTGCACCGGCACAGACATGAAGCTGCGGCTCCCTGCCAGTCCCGAGACCCACCTGGACATGCTCCGCCACCTCTACCAGGGCTGCCAGGTGGTGCAGGGAAACCTGGAACTCACCTACCTGCCCACCAATGCCAGCCTGTCCTTCCTGCAGGATATCCAGGAGGTGCAGGGCTACGTGCTCATCGCTCACAACCAAGTGAGGCAGGTCCCACTGCAGAGGCTGCGGATTGTGCGAGGCACCCAGCTCTTTGAGGACAACTATGCCCTGGCCGTGCTAGACAATGGAGACCCGCTGAACAATACCACCCCTGTCACAGGGGCCTCCCCAGGAGGCCTGCGGGAGCTGCAGCTTCGAAGCCTCACAGAGATCTTGAAAGGAGGGGTCTTGATCCAGCGGAACCCCCAGCTCTGCTACCAGGACACGATTTTGTGGAAGGACATCTTCCACAAGAACAACCAGCTGGCTCTCACACTGATAGACACCAACCGCTCTCGGGCCTGCCACCCCTGTTCTCCGATGTGTAAGGGCTCCCGCTGCTGGGGAGAGAGTTCTGAGGATTGTCAGAGCCTGACGCGCACTGTCTGTGCCGGTGGCTGTGCCCGCTGCAAGGGGCCACTGCCCACTGACTGCTGCCATGAGCAGTGTGCTGCCGGCTGCACGGGCCCCAAGCACTCTGACTGCCTGGCCTGCCTCCACTTCAACCACAGTGGCATCTGTGAGCTGCACTGCCCAGCCCTGGTCACCTACAACACAGACACGTTTGAGTCCATGCCCAATCCCGAGGGCCGGTATACATTCGGCGCCAGCTGTGTGACTGCCTGTCCCTACAACTACCTTTCTACGGACGTGGGATCCTGCACCCTCGTCTGCCCCCTGCACAACCAAGAGGTGACAGCAGAGGATGGAACACAGCGGTGTGAGAAGTGCAGCAAGCCCTGTGCCCGAGTGTGCTATGGTCTGGGCATGGAGCACTTGCGAGAGGTGAGGGCAGTTACCAGTGCCAATATCCAGGAGTTTGCTGGCTGCAAGAAGATCTTTGGGAGCCTGGCATTTCTGCCGGAGAGCTTTGATGGGGACCCAGCCTCCAACACTGCCCCGCTCCAGCCAGAGCAGCTCCAAGTGTTTGAGACTCTGGAAGAGATCACAGGTTACCTATACATCTCAGCATGGCCGGACAGCCTGCCTGACCTCAGCGTCTTCCAGAACCTGCAAGTAATCCGGGGACGAATTCTGCACAATGGCGCCTACTCGCTGACCCTGCAAGGGCTGGGCATCAGCTGGCTGGGGCTGCGCTCACTGAGGGAACTGGGCAGTGGACTGGCCCTCATCCACCATAACACCCACCTCTGCTTCGTGCACACGGTGCCCTGGGACCAGCTCTTTCGGAACCCGCACCAAGCTCTGCTCCACACTGCCAACCGGCCAGAGGACGAGTGTGTGGGCGAGGGCCTGGCCTGCCACCAGCTGTGCGCCCGAGGGCACTGCTGGGGTCCAGGGCCCACCCAGTGTGTCAACTGCAGCCAGTTCCTTCGGGGCCAGGAGTGCGTGGAGGAATGCCGAGTACTGCAGGGGCTCCCCAGGGAGTATGTGAATGCCAGGCACTGTTTGCCGTGCCACCCTGAGTGTCAGCCCCAGAATGGCTCAGTGACCTGTTTTGGACCGGAGGCTGACCAGTGTGTGGCCTGTGCCCACTATAAGGACCCTCCCTTCTGCGTGGCCCGCTGCCCCAGCGGTGTGAAACCTGACCTCTCCTACATGCCCATCTGGAAGTTTCCAGATGAGGAGGGCGCATGCCAGCCTTGCCCCATCAACTGCACCCACTCCTGTGTGGACCTGGATGACAAGGGCTGCCCCGCCGAGCAGAGAGCCAGCCCTCTGACG",
        ),
        (
            "tests/fasta_output_files/single_seq_collagen.fasta",
            ">AH002560.3 Gallus gallus collagen a2 mRNA gene, partial sequence; and precollagen alpha-2, collagen alpha-2, collagen alpha 2, collagen a2, and collagen alpha-2 genes, partial cds",
            "CCCCCGGACAGCTCCCGCTCCGACAGCCGTCGCGCTTACCGGCGCGCCCGCCGCCGGCGGGCAACAAAGCAGGGCGAGGGGCGGGGAACGTCTGAAAAAAAAAAAAAAAATCAGACGGCGAGTCAGATTTTCCTCCTGAAAGCCTCAAAGTGTCCACGTCCTCGAAGCATGGAACCAATTTAGCGCCGCCGCCGCCTTCCTCTTCCCTCCCTTCCTCCCTCCCTCGCCCCCCCCTCCGACCCCGCAGCCGAGCAGCGCCGGGCTGGGGCCGGTGGGCACGTGACAGCGCTGGGAGCCGCGCGGGCCCCGCGGCGCCGCGCGCCCATTGCTGCAGCGCCGCCGGTGCCCGCAGCCGCGGGACCCCCTGCGGTATAAATACGGCGGAGCGGGGCTTGATTAATTTAGCATCCCGGGCAGCAGGTTTCTGCTAAGTTTGGAGTTACTCCTCGCGACTGTATGCCTGCGTCCTGCAGGTAATAGCCAACCACGTCCGGGGGCTCTGCAACACAAGGAGTCTGCATGTCTAGCAAGTAGACATGCTCAGCTTTGTGGATACGCGGATTTTGTTGCTGCTCGCAGTAACTTCATACCTAGCAACAAGCCAACGTAAGTGCTTTCGCTTGTTCGTGGCATGGGTGGCGGCAGGGGGTGGCTGTCCTCGCTCCTGCGCGCTCAGGAAANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNATGTGAGTGAGNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNGGGGTGGAGATGGCCAGTCTGCCAGGCTAAATTTCATTGCACGGAAGGATTATGAGAGAACTCAGGTGTGATTTTCATTTATGCTATATTTGTAGGCTATAATAAGTATAAAATTGCCACCTTTCAACAGAAGGTCTAATGTGGTACATATATATTCACTATATAATAAACTCTTAACCTTGCTAGTAATTTAAAGAGCACAGGGCATGCTTAAGTATAGGGTGCTGACAGAAATTGTAGGGTTGAAAGGAGATGACGAATTTAAGTTTGTACATTGTATTTTTTTTAAAAAACTGATAATTTGTACCTTTTTTTTCCTAATTCTCTGCCTTATCTCTTCCAGGCATCTGCAGGGCGGAAGGTAAGCAGCTGCGTTTTTCTTGTGTGGAGATGTAGATGACATCTAAATATTCCTGAACAGAGTAATATTTTGTGGAATGTTGGATGACAAAGTGGACTAAAGTTGTTATTTCCCAGTGCTCACTGAGATGAGTAAGAATGATAAGGAGAGAACAATGGGGTGCATTAGCTTAGCAAAACGGTAAATGCAAGCTTAGGATTTAAGCTGCTTTATCCAAGAGCAGAACTAAGCATACTGAGAACCCAACTGCATCAAGAAAGAATTCTTGTTCAACAGGAGTTTCTTTGGAAGGGTTTCATGAGTTGAACAGTACAGCAGTATCCATACAGATCTGAAGGGATAAGTAGATAACCACTTTATTTTGAGAAGCGTCTCTGTTAAATAACAGACAGTTATCATGGAGAACAAAACAAACTGCCAGAGTACTTCTGTGCAGTGATTATTCAGCTGATGCAGTGGTGACAGTAACTAATTTATTTCTAGTAGCATATCGAGGCTAAAGATACACCGTGGAAAATAAGTGTAGGACCTATCCTTGCAGTCTTCTTTTCTTTTCTCATGTACACCAATGATTCTTCGTTTTCCTGTATCATCCTAGTTTCTGTGGTAACTAAGTTCTGTTTTCTTCCAACAGGGCCCTAGAGGAGACAAAGGGCCACAGGGAGAAAGGGTAAGGAAGTAGATTGACATTTATTTATTTGTGGTCTTTGAACAGTTGTTGGAAGATCAGTAGGAAAAAGCTAAGTTTAGCTATTAATAAGTTTAATGTACTTGTNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNACGGCGGACGGGCAAGGCAGTGTAAACTCAGGCTATGCTCATTTTCTGACATTAGCCATATATGTGATATTACGCATATAGCAGTGCTACAGTATGTGCTGTAGGTACCTGATTGTCTCATCACTGCAGGTTTCATAAGCTACTTTTAATGTTCACTTTATAATCCTCGTTTTGTCTCTAGGGTCCACCAGGTCCACCAGGCAGAGATGGTGAAGACGGCCCACCAGGTCCTCCAGGCCCCCCTGGTCCTCCAGGTCTTGGCGGAGTAAGACATGCAAACTTTTTATTACTGAAATTGATAATTTTTGCTTTGTGATGACTAAAGACTAAATGTATATTTACTGGCACGCTGACATTCAACTGGAGAGTAGAGCAAGCAATCTTGTGTCATTGGCATCAGATTAGTGGTCTCAGTTCCAGTGCAACTCTCCTTAGGATCTGTATCTTCCTCAGCAACTTTGGATNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNACCCTTCCTACTGAATCAAGTCTTTCTGGAAACAGATGAATAGAAATGTATTTGTAAAAGGGTCATGTGTACTGAGTTTTAAGTATGTTGCTTCAACATACTGTCTAGCAAATGAGGTAATGGATACATGTAGAATGAGGGTTATCAGTGCTTTCTGAAGTAAGAATTGTAGTGACTTTTATTTCAAATTTTTGTCATCTACAGAATTTTGCTGCTCAGTATGATCCATCTAAAGCGGCTGACTTTGGCCCCGGACCTATGGTAAGTATATGATTTAACACTTGGTAACTTGCATAAACATGTATTTAAGTGTACTCCAGNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNTTTAACAGGGTCCCCAAGGTCCTCGTGGTCCCCCTGGTCCTCCAGGAAAGGCTGGTGAAGATGTAAGTCANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNTTTTTTAGGGTCACCCTGGCAAACCTGGAAGACCTGGTGAGAGGGGTGTTGCTGGTCCTCAAGTAAGTAANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNGGGCCATTCTGTGATTCTGTGTGATTATAATGTCAGGCTAATGAAGTTACTCTGCAATTGCCCTAACACTCTGGATACTGATACAGAGCTTTATCCTTTTCTCAAACAGGGTGAAATCGGACCTGCTGGTAATGAAGGCCCTACTGGTCCTGCTGGTCCAAGAGGAGAGATTGGACTTCCTGGTTCCAGTGGTCCTGTTGGCCCTCCCGTGAGTACCTTGCCAGTCTTTATCTATTGTCAGATGGATGCATTTGAGACTGAATTAACCAGTATAATTCTTTTCTGCCTCCATAGGGCAACCCTGGTGCTAATGGTCTTCCTGGGGCTAAAGGTGCAGCTGTAAGTATAGCCACATGCACACTTATTTACTTTAAGATTAAAAAAAAATAACAACAACACACCACATTTCAGTTAATGGATCACAAAAGATAATGAACTTACAGTAGACTTTCTCTGTTTGGAACAGGGTCTTCCTGGTGTTGCTGGTGCTCCTGGTCTGCCTGGGCCCCGTGGTATTCCTGGTCCTCCTGGCCCTGCTGGTCCAAGTGGTGCTAGGGGACTTGTTGTAAGTGACTTTGTTTACTGCATGTCTTCATTTGAAAACTGGATACAGCATCCATCATTGTAAAATATTTCTTCTAGATATGTTCCTTCATTGAATGCAGACACTTTTGTTGCTTCAGTATAATTAAGCATTGTGAGCTTGTTTCTGTCTCTCAGTGAGACTGAAGAGGTTCACTTTGTACTCCCTTTGGCTGCAAGAACTATTAAGCTCTGACCCTCTTGATGGTATCAACAGAGATGTGACAGCAGTCTCACAATCAGAACCTCAAGGGGTATCCCCAGTAGAGGAACCAGCCCAGAGCGTTTCTTAATTCAATTACTGTAATTTCTAAACATCTTCAACATGTTTGTTTTCATGCCTATTAAACCTAAAGTGCAGTTACATTAACTGACTATATCAAAATAGAGTCAGGCATGACACTGGATGATTAGAGATGGTTGTGATTCATGATAATGTTGTACAGGTAGAAGAAAGATCTGTAGAATGGTGCTTAATTCTAGAATCTCTTTTTATGTTGGACTCTAGGGTGAACCAGGCCCTGCTGGTGCCAAGGGAGAAAGTGGTAACAAGGGTGAGCCTGTAAGTATGGCAATTTGTGAGTGTTGTTTCAATGAATATAGTCTCATAGTACCTAGTAGCTCAGCTCTAATTTATTCTTTTCCTCTTGGCTGAGGTAGGGTGCTGCTGGCCCCCCTGGCCCTCCTGGTCCAAGTGGTGAGGAAGGCAAGAGAGGCAGCAATGGTGAACCTGGCTCTGCTGGTCCCCCTGGCCCTGCTGGTCTAAGAGTAAGGTTTTTTTTCATGTTCCAGAAGAAAAAAACAAAAAGGAAAGAAGAAATAAAGCTATATCTGCAAAGGGAAATTAAATAATTATAAATGACTACATTTGTGTTAATGCAACTAGGCAAAGGTCATTTTGCTGTTCTGTGCCTTTTGATTTGCTGGGACCACCCTAATTTTTGTTTTGCATTAATGATGTTTATTATCTTATCCCTGAATTAATTTAAGGTTGCTTTGTGTTATCCACTGATTAATATTTAGAGAAATAGCACTAACTTTGCTGTGAAGCTTGAGATATAAGTGCTCGAAAGAGATAGTTGGCTCACATGTAATGTTTGGGAGAGGTTTAAGTTCAGTGCCTTCGAGGGTATCTGTAGTACGCTTATCACAGGGCGAGGAAACAACACAATGTCTTTCAGGAGGCACGTAGCTTTGAGCAGGTGCAGGTGTAGGAANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNAACGGGAACAGAGTTTTCTTTCCTTTTTCAGATTTAATTTGTATTCACTTGCAGGGCGAGCCTGGATCTCGTGGTCTCCCTGGAGCTGATGGCAGAGCTGGTGTCATGGTAAGGCTTGTCTCTGAATCATTATTTCTAAACCATCTTCTTTTATATACAAATGTGTGATGCTTTTTGCTACCTATTCCTAATTTTATTTATTTCTTTTGTTGTTAGGGACCTGCTGGTAACCGTGGTGCTAGTGGACCTGTTGGTGCTAAGGGTCCTAATGGTGATGCTGGCCGTCCTGGTGAACCTGGTCTTATGGGTCCAAGAGTAAGTCTAGAACTGTGCAAAAAGAAACTACTTGTATTTGTGGTAAATTATCAGAAATCCAATTGCAGGAAGTTCTATTCAAGCCACAATTAGACTGTTTCTATCAGCCCACTGAAAAAACATCCGTGAGGGAATGATTAAGCAGCATCAAAATGTTTATTGAAATTCATTTCTTTAGTAATCTGGTGGCATCTAATTGCCTTGGCCATGGNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNTTTTCTAGGGTTTCCCTGGAGCAGATGGTAGGGTTGGGCCAATCGGTCCAGCCGGTAATAGAGGTGAACCTGGCAACATTGGATTCCCTGGACCAAAAGGTCCCACTGTAAGTACNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNACCTTCAGGGTGAGCCTGGCAAACCTGGTGAAAAAGGCAATGTCGGTCTTGCTGGCCCACGGGTACGTGGNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNGGCAAACCAGGCGAAAGGGGTCTCCATGGTGAATTTGGTGTCCCTGGTCCTGCTGGCCCAAGGGGCNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNTTCAACAGGGCAATCCTGGAAATGATGGTCCTCCAGGCCGTGATGGTGCTCCTGGCTTCAAGGTAGACTTNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNGTTCACAGGGTGAGCGTGGTGCTCCTGGTAACCCAGGTCCCNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNGGTCCTTCTGGAAAGCCTGGAAACCGTGGTGATCCTGTAAGTTGNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNTGTTCCAGGGTCCTGTTGGTCCTGTTGGTCCTGCTGGTGCTTTTGGCCCAAGAGGTCTCGCTGTAAGTCTNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNGGATTAACACTTTTCATGGGTGTCTTAACAGAATACACATAAATATATCAGGGGCCACCTGTGGCAATGCAGAACACTTAATTCATTCTTTGTCAGTAATATCTAATTCAGGCCTTCTCTGGCATGTATATCCTTTCCTAGGGCCCACAAGGTCCACGTGGTGAGAAAGGTGAACATGGTGATAAGGGACATAGAGGTCTGCCTGGCCTGAAGGGACACAATGGGTTGCAGGGTCTTCCTGGTCTTGCTGTAAGTAAATGATTTTCAGTAATTTTTTTGGTNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNATAAGATCCAAACACTCGGTCTCCACATAATAGAGATGAGAANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNAACAGTCTCTTATTTTAAAGGCTTTACTGGAAACCCTAAGAGACAATACAAGAGACTACTATAGGTTATACCTTTAAATAACTTTTTTACTCACTTTCCTCCCACATTTTATATCCCAACTCCACTAATGCCAGTTGCCCAAGATTTCAGTTCTCTGAACCCAAATATGTCTGCTGATCCCCTCTTGAATCATGTTAATACAATGTGTGGCATTGCATTTTTTAATGATGCATTTCTTTTCCCAATAGGGCCAACATGGTGATCAAGGTCCTCCTGGTAACAACGGTCCAGCTGGCCCAAGGGTATGTGAATTCAAGAGTATATGCAAATAATTCTCCTATTCCTTTTATGGAATATATTTGTACACTGTCCTTTGTATGAANNNNNNATTTGTAGTGTTCCCTACTGTTGTTAAACTGTTCAAGTTTTCTTCTAGGGTCCTCATGGTCCTTCTGGTCCTCATGGTAAGGATGGTCGCAATGGTCTCCCTGGACCCATTGGCCCTGCTGGTGTACGTGGATCTCATGGTAGCCAAGGCCCTGCTGTGAGTANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNCTTATGGCCAGCCAGTATAAGCACAAAGGTTTGGTAGTTCCACACAGTGTATCTTCTGCTTCAGTTCACAGGAGTTACCACAGAGCAGGTCCATAGGTCCTTCCTCAGATTATTGTTGAGGGTTCTAAGACTTCAGAAGGACAACGCATGTGTGGAAATAGTCAGCTGAAAGTATCATAAATGTGATAGAATACTAATTGTCTTTTGCTTTTGAAAAACTTTAGGGCCCTCCTGGCCCTCCTGGTCCCCCCGGCCCCCCTGGTCCCAATGGTGGCGGATATGAAGTTGGCTTTGATGCAGAATACTACCGGGCTGATCAGCCTTCTCTCAGACCCAAGGATTATGAAGTTGATGCCACTCTGAAAACATTGAACAACCAAATTGAGACCCTGCTGACCCCAGAAGGCTCCAAAAAGAATCCGGCTCGCACCTGCCGTGACCTCAGACTTAGCCACCCAGAATGGAGCAGCGGTACGTGGTGCCAGATGTTTCCTCTTTCTGGCTCAGCATAGTTATTTTCAGCTTATTAGCTTTCTTTTGGTNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNCCGCGAGGCGCCTCTCGTCCTCAAGGGTTTCTCCTGGATTGCGCCTAACCACGGCTGTACTGCAGATGCCATTAGAGCATACTGTGACTTTGCTACTGGTGAGACTTGCATCCATGCTAGCCTTGAAATAATTCCGACTAAGACATGGTATGTCAGCAAGAACCCCAAGGACAAAAAGCACATATGGTTCGGTGAAACTATCAATGGTGGTACTCAGGTATGTGATGCATTGGAGGATGATTGTTTCCTACAGTGCTTTTTAAGAATTTGCTACNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNCTCTCAGTGAGCTTAACTCATTTTTTAATCTCTTAGAGGAGAAATACAAAATGGGGNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNCCATTTCTAACGGAATCCTGTCTGGAATATGCTACTTTAGTACAAAGACAGTCCAGAAACAGAGAAAGTAATGAAATAATTTTTGCAATCTTTTAAATTGGGATTTATTTTTGACATATTGTGCTAGTTCAAAGGAATTGATATTTTTATTACACTGAAACTTGAAANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNTTACTAGTATGTTAGATATTGTTACCAAGCCTGCTGGAAAGTCCTTTCTGTACAATTAAGAAGAACTAATTTCATAATTTTTAAAAGAAATTGAGTTAGTCTTATGATGAAATCCCAATTTACAAGTTCTTCAATATAAAAACAAAGTTTATCACTGGGTCAGAACAAGGACCCAAGGTACTCTANNNNNNNNNNGATCATATTTCTCACATTGGCTGAAAGCGTTGCTGGTAAAGAATATAAGGAAGCAAATATTCATAACATCCACAGACACTACTCTAAAACTAAAATAAGAAATAAAAAATCAGGGCTTTCTTGAGCTTGGGCATTGTCTATATTAATNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNGGTGTGGTGGTTTCTTGTCTTTTTCAGTTTGAATACAATGGTGAAGGTGTGACCACAAAGGACATGGCCACCCAACTTGCCTTCATGCGTCTGCTGGCCAACCATGCCCCTCAGAACATCACCTACCACTGCAAGAACAGCATTGCCTACATGGATGAGGAGACTGGAAACCTTAAAAAGGCTGTTATACTCCAGGGATCCAATGATGTTGAACTACGAGCTGAAGGCAACAGCAGATTCACTTTCAGTGTTCTTGTGGATGGCTGCTCTGTAAGTAACACAGAAAGCATGGGCAGTATGATTGTATTAAAGACAGTTCTACTTTGATTCAGAACTAGATTATCAGGCAGACCAGAAACATTTTATCCAGTGAGGATAAATAGCCTGTAGAACCAACTACGCCATGTCTTTAATGAGTGGCAAAGACTGGTGTACTAACAGATCCTTCCTGCACTGTGCAATGTGGCAAAGAAAAGANNNNNNNNNNGCTTTTCTGAAGAACCAGACCCAAATTCCGTGGAAACCGAAGCATGCCGAGAAAGTAGCACAAAAGGTGCAGGAGGGCAGAGTCGAGTCGAGTCTTCAAAAGATCAGGCAAGGTTCTCTGAGGTTCAATCAGCACGAATAATACGGAAATATAGAACACACATGTANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNTTCTAATACTGCTTCTCTTGCAGAAAAAGAACAACAAATGGGGCAAAACGATCATTGAGTACAGAACAAATAAGCCGTCTCGCTTGCCCATCCTTGACATTGCACCTTTGGACATTGGTGGCGCTGACCAAGAATTCGGTTTGCACATTGGCCCAGTCTGTTTCAAATGAATGAACTAAAATTAACTTAAAGGCCCCCCCCTCAGAATTATTCTTTGTCATTTCTTTTTGTAATGAGAGCTGACTCCTTCCATTTTTTTTCTGTTCA",
        ),
        (
            "tests/fasta_output_files/single_seq_foxo3.fasta",
            ">KY421028.1 Andrias davidianus foxo3 mRNA, complete cds",
            "ATGGCCGAAGCCCCGCAGGCGGTGGACATTGACCCAGACTTCGCACCGCTCTCGCGGCCACGTTCGTGCACCTGGCCGCTGCCCCGGCCGGAGCTGGGCGCCGGGCCGCTGCCCCCGGACCCCTCGTGCGGGGGCTCCCCGCTAAGCGCCCCCGGGGGAGGTCAGCCGTCTGCCCCCGAGGGATGCGGGGACTTCAGCCGCGACTTCCTGAGCCTGCTGGAGGAGAGTGAGGCGGCGGGGGGCTGCTGCGGGAACTTTAGCTGCGGGGAGGTGGGCTGCTGCGTGCCCCCCGCGCCGCCGCAGCCCGCCCCACCGCTGCAGCAGCAGGTGCCGCCCCGCAAGAGTAGCACCTCCCGCCGCAACGCCTGGGGCAACCTGTCTTACGCCGATCTGATCACCAAGGCCATCGAGAGCTCGCCCGAGAAGCGCCTCACCCTGAGCCAGATCTACGACTGGATGGTGAAGAGCGTGCCCTACTTCAAGGACAAGGGCGACAGCAACAGCTCCGCCGGCTGGAAGAATTCGATCCGGCACAACCTATCACTTCACAGCAGATTCATCAGGGTACAGAACGACAGCACTGGGAAAAGTTCCTGGTGGATGATCAACCCTGAAGGTGGGAAAGGTGGGAAAGCTCCGCGGAGACGTGCGGTTTCAATGGACAATAGCAACAAGTACACGAAAAGCCGGGGAAGAGCTGCAAAGAAAAAGGCAGCTAATCAGGCTACGCAGGAAGCCGCTGAGGACAGTCCTTCCCAGCTCTCCAAATGGCCGGGGAGCCCCACTTCCCGCAGCAGTGACGAATTAGACGCATGGACAGATTTCCGTTCACGTACAAACTCTAATGCCAGTACAATAAGCGGCCGTTTGTCTCCTATATTGGCTACCACAGAGCTAGATGATGTTCAGGATGATGACTCGCCACTATCCCCCATGTTGTACGGAAGTCCAGGAAGCATGTCTCCGTCTATTACTAAACCAAGCACTGTTGAGTTGCCTAGGTTGACTGATATGGCAGGGACTATGAACTTGAATGATGGACTGACGGAGAACCTCATGGACGACCTTTTGGACAATATAACCCTCACCTCTTCCCAGCAGTCACCTCCAAGTGGCCTCATGCAGCGAAGCTCTAGCTTTACTTATGGTTCCAAAGCTGCAGGCCTCAGTTCCACAGCTGCTAGCTTCAACAGTCCTATGTTTGGAGCATCTGCGTTGACTTCTCTGCGTCAGTCTCCCATGCAAACCATTCAAGAGAACAAGCAAGCAACCTTTTCTTCCATCAATCTTTATGGCAACCCAAACTTGCAGGATCTGCTGACAACAGACTCGCTAAGTCACAGCGATGTCTTGATGACACAGTCTGACCCACTCATGTCCCAGGCCAGCACAGCAATGTCTGCCCAAAATGCACGGAGGAATATCATGCTACGGAATGACCCAATGATGTCATTTGCAGCACAGTCCAGCCAGGAAAACTTAATCATTCAGAACTTGCTCCACCACCAGCATCCCTCACAGAATTCCTCACTCGGTGGTGGCCGTGTCCTCTCAAATTCCATGGGAAACATTGGCTTGCATGACTCCAGCAACCTTGATTCTCCTAAGCACCAGCAACTGTCATCTGTCAATCAGTCTATGCAAACATTTTCTGACTCGCTCTCTGGCTCTTTGTACTCCACAAGTGTGAACCTTCCAATCCTGGGCCACGAAAGGTTTCCGAGTGACTTGGACCTGGATATTTTCAGTGGGAGTTTGGAATGTGACATGGAATCCATTATCCGCAATGAACTGATGGATGCAGATGGGTTGGATTTTAACTTTGACTCCCTCATCTCAGCTCAGAATGTTGTGTCGCTGAATGTGGGGAACTTCACGGGTGCTAAGCAAACTTCATCACAGAGTTGGGTGCCGGGCTGA",
        ),
    ],
)
def test_fasta_read_write(filepath, header, seq):
    genecomb_input = GeneComb(seq=seq, header=header)
    genecomb_input.write_to_fasta_file(filepath)
    genecomb_output = read_fasta(filepath)
    assert genecomb_input.header == genecomb_output.header
    assert genecomb_input.seq == genecomb_output.seq


# TODO override changing using files for testing to using a standard output
