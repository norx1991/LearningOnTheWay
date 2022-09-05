import os

os.chdir("./src/")

with open("SUMMARY.md", 'r') as summary:
    lines = summary.readlines()
    with open("toc.md", 'w') as toc:
        for line in lines:
            if line.startswith(r'      '):  # Only include up to Level-2 title
                continue
            if '/README.md)' in line:
                line = line.split('[')[1].split(']')[0] + '\n'
            toc.write(line)
