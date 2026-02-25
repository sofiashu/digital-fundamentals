files = ["seq1", "seq2", "seq3", "seq4"]
date = "08/11/2067"

for name in files:
   new_name = name + date + ".fasta"
   print(f"{new_name}")
