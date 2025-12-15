import sys

with open(sys.argv[1], encoding="utf-8") as fin, \
     open(sys.argv[2], "w", encoding="utf-8") as fout:
    for r in fin:
        fout.write(r.strip().lower().replace(" ", "-") + "\n")
