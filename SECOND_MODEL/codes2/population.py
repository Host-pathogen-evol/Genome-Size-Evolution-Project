def N_calc(path_pop,path_r,el,N_old,NH):
    sommatoria=0
    Ni=N_old
    sommatoria=sum([path_pop[x][1][-1]*path_r[x] for x in path_pop])
    Ni_t1=((path_r[el]*NH*Ni)/((0.001*NH)+sommatoria))#-Ni
    if Ni_t1<1:
        Ni_t1=0
    return Ni_t1
