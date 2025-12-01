# imports
import os
import csv
import sys
import subprocess
import tempfile
import shutil
import json
import struct
import numpy as np
import pandas as pd
from ersilia_pack_utils.core import read_smiles, write_out

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

temp_dir = tempfile.mkdtemp(prefix="ersilia_", dir=root)
input_file_ = os.path.join(temp_dir, "normalized_input.csv")
output_file_ = os.path.join(temp_dir, "normalized_output.csv")

# read input
_, smiles_list = read_smiles(input_file)


#Create intermediate input
with open(input_file_, "w", newline="") as f:
	writer = csv.writer(f)
	writer.writerow(["smiles"])
	for s in smiles_list:
		writer.writerow([s])

# my model
subprocess.run(["python", os.path.join(root, "gather_representation.py"),
	"--gpu", "cpu",
	"--output_filepath", output_file_,
	"--smiles_filepath", input_file_,
	"--smiles_colname", "smiles",
	"--chemid_colname", "smiles",
	"--representation", "gin_concat_R1000_E8000_lambda0.0001"], 
	stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


# Compare SMILES input and output
smiles_input = smiles_list
smiles_output = pd.read_csv(os.path.join(output_file_), sep=',').iloc[:, 0].tolist()
assert smiles_input == smiles_output

# Change output format
output = pd.read_csv(os.path.join(output_file_), sep=',')
output = output.iloc[:, 1:]
results = output.values.tolist()

header = [f"dim_{i:03d}" for i in range(len(output.columns))]

write_out(results, header, output_file, np.float32)

shutil.rmtree(temp_dir)
