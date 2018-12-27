#!/usr/bin/python3

# Dictionary of Monoisotopic masses
monoIsoDic = {'A':71.0371, 'C':103.0092, 'D':115.0269, 'E':129.0426,
              'F':147.0684, 'G':57.0215, 'H':137.0589, 'I':113.0841,
              'K':128.0950, 'L':113.0841, 'M':131.0405, 'N':114.0429,
              'P':97.0528, 'Q':128.0586, 'R':156.1011, 'S':87.0320,
              'T':101.0477, 'V':99.0684, 'W':186.0793, 'Y':163.0633, '*':0.0}

# Dictionary of Average masses
avgMassDic = {'A':71.08, 'C':103.14, 'D':115.09, 'E':129.12,
              'F':147.18, 'G':57.05, 'H':137.14, 'I':113.16,
              'K':128.17, 'L':113.16, 'M':131.19, 'N':114.10,
              'P':97.12, 'Q':128.13, 'R':156.19, 'S':87.08,
              'T':101.10, 'V':99.13, 'W':186.21, 'Y':163.18, '*':0.0}

import sys     # Importing in the sys module
import argparse     # Importing in argparse module to create arguments for user input
parser = argparse.ArgumentParser(description = 'Read in a Fasta format file to convert sequence information into mass-to-charge values. These can either be in monoisotopic masses or average mass values.') # Create Argparser object
parser.add_argument('-input', help = 'Please input your Fasta format file path.') # Create argument for user to supply input file
parser.add_argument('-output', default = 'AnalysedMasses', help = 'Please give your output file a name. The default is "AnalysedMasses" and all files will save with an extension of ".pepmasses".') # Create argument for user to supply output file name
parser.add_argument('-c', default = 1, type = int, help = 'Input charge value of either 1, 2 or 3.') # Create argument for user to provide charge value
parser.add_argument('-i', default = avgMassDic, help = 'Choose either monoisotopic [m] or average [a] mass values.') # Create argument for user to choose which dictionary of masses to use
args = parser.parse_args()

# Defining a function for opening a file and stripping the important details
def readFastaFile(): # Define function for opening a fasta file
    fileObj = open(args.input, 'r') # Read in and open fasta file
    headerName = []     # List for header starting with >
    seq = {}        #Sequence Dictionary
    for line in fileObj:
        if line.startswith ('>'):     # If line starts with '>' then do the following:
            header = line[1:].rstrip('\n') #remove newline
            headerName.append(header) # Add stripped header to the header list
            seq[header] = ''
        else:
            seq[headerName[-1]] += line.rstrip('\n') # If line doesn't start with '>' strip next line into seq dictionary which would be the sequence
    fileObj.close()
    return (seq, headerName)

(massSeqs, seqHeaders) = readFastaFile() # Call in the file opening function

# If statement to error check so that user can only choose either monoisotopic or average masses and if not the code won't run using the sys module
if args.i == 'm': # If user chooses 'm' the mass dictionary chosen will be monoisotopic
    massDict = monoIsoDic
elif args.i == 'a': # If user chooses 'a' the mass dictionary chosen will be average masses
    massDict = avgMassDic
elif (args.i is not 'a') or (args.i is not 'm'): # If 'a' or 'm' are not chosen print an error message and stop the program
    sys.exit('Error: Please choose either "a" to use average masses or "m" for monoisotopic masses. Try Again.')

# If statement to error check what the charge value is and to stop the code running if the parameters aren't met
if args.c == 3: # If user chooses charge as 3 set charge as 3
    charge = 3
elif args.c == 2: # If user chooses charge as 2 set charge as 2
    charge = 2
elif args.c == 1: # If user chooses charge as 1 set charge as 1
    charge = 1
elif (args.c is not 1) and (args.c is not 2) and (args.c is not 3): # If user doesn't choose 1, 2 or 3 print error message and stop the program
    sys.exit('Error: Please choose either 1, 2 or 3 as your charge value. Try Again.')

# If statement to error check whether the user input for the output filename includes their own extension which is not allowed as the program adds its own extension of ".pepmasses"
if "." in args.output: # If "." is in the output file name the program will print an error message and exit
    sys.exit("Error: Please don't include your own extension as the program will write the output file with the '.pepmasses' extension. Try Again.")

# If statement to change the water mass value depending on which mass dictionary is chosen by the user
if massDict == avgMassDic: # If user chooses average masses set water to the given value
    water = 18.0153
elif massDict == monoIsoDic: # If user chooses monoisotopic masses set water to the given value
    water = 18.0106

# Calculate the mass to charge values for each sequence and add them to a list which will be written to the output file
outputs = [] # Create empty list for output file
for header in seqHeaders:
    sum = 0
    for character in massSeqs[header]: # For each character in the sequence:
        mass = massDict[character] # The mass equals the value of the matched key in the chosen dictionary to the amino acid in the sequence
        sum = mass + sum
        massCharge = sum + water + charge # Mass to charge value of mass values, water value and charge
        finalMass = massCharge / charge # Final mass to charge ratio by dividing by the charge value chosen by the user input
    outputs.append('{:12}\t\t{}\t{:10.4f}\t{}\t{}'.format(header.split()[0], header.split()[2], finalMass, charge, massSeqs[header])) # Add final formatted data to the outputs list seperated by tabs

# Writing the output to a file
outputFileName = args.output + ".pepmasses" # Add '.pepmasses' extension to the output filename supplied by user
outputFile = open(outputFileName, 'w') # Create the output file depending on what the user names the file
for line in outputs: # For each line in the output list:
    outputFile.write(line + '\n') # Write to the output file seperating each line by '\n' (newline value)






