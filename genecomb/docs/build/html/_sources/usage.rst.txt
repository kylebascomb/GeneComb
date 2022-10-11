Usage
=====

Installation
------------

To use genecomb, first install it using pip:

.. code-block:: console

   (.venv) $ pip install genecomb


Counting Bases
--------------
To count the bases in a genecomb sequence, 
you can use the ``GeneComb.base_counter`` function:

.. autofunction:: genecomb.GeneComb.base_counter


Calculating GC Content
----------------------
The GC content of a sequence is the percentage of G's and C's in the nucleotide sequence.
To calculate the GC content of a GeneComb sequence, you can use the 
``GeneComb.gc_content`` function:

.. autofunction:: genecomb.GeneComb.gc_content


Finding the number of Non-nucleotide Bases
------------------------------------------
It can be helpful to know the number of bases in a sequence that are not a valid 
nucleotide (A, C, G, T). You can quickly calculate this value using the 
``GeneComb.non_nucleotide_counter`` function:

.. autofunction:: genecomb.GeneComb.non_nucleotide_counter


Finding all palindromic subsequences
-------------------------------------
A palindromic sequence is a nucleic acid sequence in a double-stranded DNA or RNA molecule whereby reading 
in a certain direction (e.g. 5' to 3') on one strand is identical to 
the sequence in the same direction (e.g. 5' to 3') on the complementary strand 
`[Source] <https://en.wikipedia.org/wiki/Palindromic_sequence>`_.
You can calculate all the palindromic sequences using the 
``GeneComb.find_palindromes`` function:

.. autofunction:: genecomb.GeneComb.find_palindromes


Transcribing a nucleotide sequence to RNA
------------------------------------------
Transcribing a DNA nucleotide sequence to RNA can be done using the
``GeneComb.get_rna_transcription`` function:

.. autofunction:: genecomb.GeneComb.get_rna_transcription


Translating a nucleotide sequence to protein bases
---------------------------------------------------
It can often be helpful to translate your nucleotide sequence into the corresponding protein sequence. This can
be done using the ``GeneComb.translate_to_protein`` function:

.. autofunction:: genecomb.GeneComb.translate_to_protein


Counting point mutations between two sequences
----------------------------------------------
A point mutation is when two sequences that should be identical have a mismatch in a position. This can occur due to mutations 
in a sequence. To count the number of point mutations between two equal length sequences, you can use the 
``genecomb.count_point_mutations`` function:

.. autofunction:: genecomb.count_point_mutations


Writing a GeneComb sequence to a FASTA file
--------------------------------------------
You can write a GeneComb nucleotide sequence to a FASTA file with the
``GeneComb.write_to_fasta_file`` function:

.. autofunction:: genecomb.GeneComb.write_to_fasta_file


Reading GeneComb sequences from a FASTA file
---------------------------------------------
You can read a sequence (or multiple sequences) from a valid FASTA formatted file with the
``genecomb.read_fasta`` function:

.. autofunction:: genecomb.read_fasta
