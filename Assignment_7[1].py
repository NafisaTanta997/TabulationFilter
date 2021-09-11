
"""
Name: Nafisa Tanta
Email: Nafisa.Tanta67@myhunter.cuny.edu
Resources: Question prompt for Program 7
"""

import pandas as pd
import pandasql as psql

# Input file name
fileInput = input("Enter input file name: ")

# Output file name
fileOutput = input("Enter output file name: ")

# Read input fileInput
readfile = pd.read_csv(fileInput)


q = 'SELECT NTACode, NTAName FROM readfile'

nta_ = psql.sqldf(q)

# Selecting these columns
data_nta = {"NTA": nta_["NTACode"], "NTA_Name": nta_["NTAName"]}

# Load data into data frame
df = pd.DataFrame(data_nta)

# convert data frame to the csv output file
df.to_csv(fileOutput, index=False)

print(df)
