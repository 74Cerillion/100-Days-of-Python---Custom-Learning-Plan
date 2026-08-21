
import hashlib
from pathlib import Path
import sys

def main():
  parsed_dir = input("Enter directory to parse: ")

  while True:
    p = Path(parsed_dir)
    if p.exists() and p.is_dir(): # Ensure it's a directory
      break
    else:
      parsed_dir = input("Invalid Directory. Enter valid directory (or 'q' to quit): ")
      if parsed_dir == 'q':
        sys.exit()

  dups = find_dups(p)
  if dups:
    print("\nFound duplicate files (grouped by hash value):")
    for hash_val, files in dups.items():
      print(f"  Hash: {hash_val}")
      for f in files:
        print(f"    - {f}")
  else:
    print("\nNo duplicate files found in the specified directory.")

def find_dups(directory_path):
  hash_to_files = {} # Dictionary to store hash_digest -> [list of file paths]
  chunk_size = 4096 # Read in 4KB chunks

  for file_path in directory_path.rglob('*'): # Iterate recursively over all files and subdirectories
    if file_path.is_file(): # Process only files
      hasher = hashlib.sha256()
      try:
        with open(file_path, 'rb') as f: # Open in binary read mode
          while True:
            chunk = f.read(chunk_size)
            if not chunk:
              break
            hasher.update(chunk)
       
        file_hash = hasher.hexdigest() # Get the hexadecimal digest of the hash

        if file_hash in hash_to_files:
          hash_to_files[file_hash].append(file_path)
        else:
          hash_to_files[file_hash] = [file_path]
      except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        continue
 
  # Filter out files that don't have duplicates
  duplicate_groups = {hash_val: files for hash_val, files in hash_to_files.items() if len(files) > 1}
  return duplicate_groups

if __name__ == "__main__":
  main()