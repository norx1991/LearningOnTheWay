import os

questions = []

d = {}
for line in open("question-list.md").readlines():
    number = int(line.split('.')[0].split('[')[1])
    title = line.split('[')[1].split(']')[0]
    link = line.split('(')[1].split(')')[0]
    d[number] = (title, link)

for question in questions:
    if os.path.isfile(str(question) + '.md'):
        continue
    fout = open(str(question) + '.md', 'w')
    fout.write(f'[{d[question][0]}]({d[question][1]})')
    fout.close()

for question in sorted(questions):
    print(f'[{d[question][0]}](Leetcode/{question}.md)')
