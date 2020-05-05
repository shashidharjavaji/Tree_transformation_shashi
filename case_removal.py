f=open("E_conll_parse")

text=f.read()
d=[]
ss=text.splitlines()
word=[]
parent=[]
for i in range(len(ss)-1):
    if(ss[i].split('\t')[7]!='case'):
        d.append(ss[i]+'\n')
    else:
        parent.append(ss[i].split('\t')[6])
        word.append(ss[i].split('\t')[1])
for i in range(len(word)):
    for j in range(len(d)):
        if(d[j].split('\t')[0]==parent[i]):
            res = [sub.replace(d[j].split('\t')[1], word[i]+' '+d[j].split('\t')[1]) for sub in d]
with open('delete.txt',"w") as k:
    k.seek(0)
    for l in res:
        k.write(l)
