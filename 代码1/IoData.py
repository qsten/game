def read_data():
    f=open('排行榜.txt')
    lines=[line.strip().split('\t') for line in f.readlines()]
    namelist=[line[0] for line in lines]
    scorelist=[int(line[-1]) for line in lines]
    f.close()
    return namelist,scorelist

def write_data(namelist,score):
    f=open('排行榜.txt','w')
    for i in range(4):
        f.write(namelist[i]+'\t'+str(score[i])+'\n')
    f.close()



