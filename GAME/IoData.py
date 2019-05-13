def read_data(file):
    f=open(file)
    lines=[line.strip().split('\t') for line in f.readlines()]
    namelist=[line[0] for line in lines][:4]
    scorelist=[int(line[-1]) for line in lines][:4]
    f.close()
    return namelist,scorelist

def write_data(file,namelist,score):
    f=open(file,'w')
    for i in range(4):
        f.write(namelist[i]+'\t'+str(score[i])+'\n')
    f.close()



def alt_file(stats):
    if stats.classical_mode==True:
        file='infinited_rand.txt'
    elif stats.time_mode==True:
        file='time_rand.txt'
    else:
        file='classical_rand.txt'
    return file