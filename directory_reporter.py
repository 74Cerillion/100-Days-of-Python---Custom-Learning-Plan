from pathlib import Path
import sys

def main():

    tree = input("What is the directory tree that you would " \
    "like to be searched? ")

    while True:
        p = Path(tree)
        if p.exists():
            break
        else:
            tree = input("Invalid Directory. Please try another or press 'q' to quit: ")
            if tree == 'q':
                sys.exit()

    result = examine_tree(p)

    print("\nDirectory parsed successfully!")
    sh_output(result)

def examine_tree(p):
    d = {}
    for f in p.rglob('*'):
        if f.is_file():
            if f.suffix.lower() in d.keys():
                d[f.suffix.lower()] += f.stat().st_size
            else:
                d[f.suffix.lower()] = f.stat().st_size
    return d

def sh_output(result):
    for i in result.items():
        k, v = i[0], i[1]
        print("\nExtension: {} | Size: {}KB".format(k, v/1000))

if __name__ == '__main__':
    main()