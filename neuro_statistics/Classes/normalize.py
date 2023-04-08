def normalize(data):
    fin = []
    fin2 = []
    for i in range(len(data[0])):
        fin.append([])
    for t in data:
        fin2.append([])
        for c,d in enumerate(t):
            fin[c].append(d)

    for i in fin:
        temp = max(i)
        if temp != 0:
            for e,x in enumerate(i):
                i[e] = x/temp

    for f in fin:
        for d,i in enumerate(f):
            fin2[d].append(i)

    return fin2
