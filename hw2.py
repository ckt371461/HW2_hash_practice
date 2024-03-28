with open('hw2_data.txt','r') as f:
    dic = dict()
    for line in f.readlines():
        line = line.strip()
        if line in dic:
            dic[line] += 1
        else:
            dic[line] = 1
print(len(dic))
print(dic)