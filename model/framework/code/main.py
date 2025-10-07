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

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

temp_dir = tempfile.mkdtemp(prefix="ersilia_", dir=root)
input_file_ = os.path.join(temp_dir, "normalized_input.csv")
output_file_ = os.path.join(temp_dir, "normalized_output.csv")

# functions to read and write .csv and .bin files
def read_smiles_csv(in_file): # read SMILES from .csv file, assuming one column with header
  with open(in_file, "r") as f:
    reader = csv.reader(f)
    cols = next(reader)
    data = [r[0] for r in reader]
    return cols, data

def read_smiles_bin(in_file):
  with open(in_file, "rb") as f:
    data = f.read()

  mv = memoryview(data)
  nl = mv.tobytes().find(b"\n")
  meta = json.loads(mv[:nl].tobytes().decode("utf-8"))
  cols = meta.get("columns", [])
  count = meta.get("count", 0)
  smiles_list = [None] * count
  offset = nl + 1
  for i in range(count):
    (length,) = struct.unpack_from(">I", mv, offset)
    offset += 4
    smiles_list[i] = mv[offset : offset + length].tobytes().decode("utf-8")
    offset += length
  return cols, smiles_list

def read_smiles(in_file):
  if in_file.endswith(".bin"):
    return read_smiles_bin(in_file)
  return read_smiles_csv(in_file)

def write_out_csv(results, header, file):
  with open(file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for r in results:
      writer.writerow(r)

def write_out_bin(results, header, file):
  arr = np.asarray(results, dtype=np.float32)
  meta = {"columns": header, "shape": arr.shape, "dtype": "float32"}
  meta_bytes = (json.dumps(meta) + "\n").encode("utf-8")
  with open(file, "wb") as f:
    f.write(meta_bytes)
    f.truncate(len(meta_bytes) + arr.nbytes)
  m = np.memmap(
    file, dtype=arr.dtype, mode="r+", offset=len(meta_bytes), shape=arr.shape
  )
  m[:] = arr
  m.flush()

def write_out(results, header, file):
  if file.endswith(".bin"):
    write_out_bin(results, header, file)
  elif file.endswith(".csv"):
    write_out_csv(results, header, file)
  else:
    raise ValueError(f"Unsupported extension for {file!r}")

# read input
_, smiles_list = read_smiles(input_file)

# create intermediate input
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

write_out(results, header, output_file)

shutil.rmtree(temp_dir)
