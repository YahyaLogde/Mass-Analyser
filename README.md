# Mass-Analyser
**NAME**

Mass Analyser – Determines the mass-to-charge (M/Z) value for amino acid sequences.

**SYNOPSIS**

MassAnalyser.py	
-h --help
-input 
-output 
-c [1] [2] [3]
-i [m monoisotopic] [a average]

**DESCRIPTION**

Mass Analyser is a program that is used to calculate the mass-to-charge ratio of amino acid sequence information derived from digested proteins. This information is read into the program in the Fasta file format. The program copes with both monoisotopic and average mass values to calculate the mass-to-charge value for each sequence coinciding with what charge (1, 2 or 3) the user inputs. The program also takes into account the mass of water due to them being single residue.
| Protein Name | Peptide No. | Mass-to-Charge | Charge | Sequence |
The output file displays the results in a simple text file as columns with the following content:

**OPTIONS**

-h --help

	Shows the programs help message and exits.
-input

    Allows giving the file path that has the sequence data that needs converting into mass-to-charge ratios.
-output

    Allows naming of the output data file. The default extension is “.pepmasses”, this cannot be changed.
-c charge

    Provide the charge value for the peptide sequences, they can only be either 1, 2 or 3. The default is 1.
-i isotope type, m monoisotopic, a average

    Set which isotopic mass values to use, either monoisotopic or average mass values.
**EXAMPLE**

	MassAnalyser.py -input input.fasta -i a -c 1 -output AnalysedMasses
**AUTHOR**

   Written by Yahya Logde, Yahya.logde@postgrad.manchester.ac.uk.

