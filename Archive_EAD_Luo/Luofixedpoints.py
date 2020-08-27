# Clear directory - remove junk from previous runs and start fresh
clean()
name = "Luofixedpoints"
delete(name)

# Continue down in capacitance
#c = load(e=name,c="constants",ICP=[1],UZSTOP={1 : 0.25})#, UZSTOP={3:[0,1]})
#c1 = run(c)

#l = load(c1('UZ1'),ICP=[4])#, UZSTOP={3:[0,1]})
#r = merge(run(l) + run(l,DS='-'))

# Compute bifurcation diagram with DS>0 and save results
l = load(e=name,c="constants",ICP=[2], NMX=1000, UZR={2: 3.0}, STOP=['UZ1'])
r = run(l,DS='-')
#r = run(l)
#sv(r,name)

s = run(r('UZ1'), ICP=[4], UZR={4: 0.123}, STOP=['UZ3'], DS='-')
sv(s,name)

# Continue down in capacitance
#c = run(s('UZ1'),ICP=[1,16,17,18,19], UZSTOP={1 : 0.0}, DS= -0.001, DSMAX=0.005)#, UZSTOP={3:[0,1]})
#sv(c,name)
#c1 = run(s('UZ1'),ICP=[1], UZR={1 : 1.0}, STOP=['UZ2'], DS= 0.001)
#ap(c1,name)

#h = run(c('HB1'), UZR={1: 1}, STOP=['UZ2'], IPS=2, DS= '-')
#ap(h,name)

#h = run(s('HB1'), UZSTOP={}, UZR={2: 3.0}, SP=['LP2','UZ2','BP0'], DS='-', IPS=2)
#ap(h,name)

# Grab the first Hopf bifurcation and continue the periodic orbit
hr1=run(s('HB1'),IPS=2,ISW=-1,ICP=[4,11],UZSTOP={11:6000},DS=0.005) #ISP=2
ap(hr1,name)

# Grab the second Hopf bifurcation and continue the periodic orbit
#hr2=run(r('HB2'),IPS=2,ISW=-1,ICP=[2,11],UZSTOP={11:120000},NMX=2000,ISP=4,ILP=1) #ISP=2
#ap(hr2,name)

#wait()

# Continue period-doubling bifurcation
#pd1 = run(hr1('PD1'),NTST=750,ISW=-1, STOP=['UZ1'])
#ap(pd1,name)

#pd2 = run(pd1('PD1'),NTST=1000, ISW=-1)
#ap(pd2,name)

#pd3 = run(pd2('PD1'),NTST=1250, ISW=-1, DSMAX=0.05)
#ap(pd3,name)

#pd4 = run(pd3('PD1'),NTST=1500, ISW=-1, DSMAX=0.05)
#ap(pd4,name)

#p2 = load(e="L1s2mmo",c="L1s2mmo",ICP=[2,11],IPS=2,NMX=1000,ISP=4,ILP=0)
#pd2 = run(p2,DS='-')
#ap(pd2,name)

#Continue locus of Ko_LP1
#t = load(r('LP1'),ICP=[2,4],ISW=2, DS = 0.01,DSMAX=0.01, UZSTOP = {2:5.4},NMX=5000)
#t1 = merge(run(t) + run(t, DS='-'))
#sv(t1,name)

#loadbd(name).writeRawFilename('2LP1')

# Compute locus of Hopf in two parameters
#h = load(s('HB1'), ICP=[4,2], ISW=2, UZSTOP={2:2},DS=0.001)
# Continue from this label in two parameters
#h2 = run(h)
#sv(h2,name)

# Compute locus of SNP in two parameters
#s = load(hr1('LP1'),ICP=[4,2], ISW=2, ISP=1, UZSTOP={2:[0,5.4]}) #no detection of folds
# Continue from this label in two parameters
#s1 = run(s)
#sp = merge(run(s1) + run(s1,DS='-'))
#sv(sp,name)

#loadbd(name).writeRawFilename('2Hopf_C025')
#bifdiag=loadbd(name).toArray()

# Compute locus of Homoclinic orbit in two parameters
#ho = load(hr1('UZ1'), ICP=[4,2], ISP=0, UZSTOP={2:0.00001},NMX=1000) #NWTN 50 100
# Continue from this label in two parameters
#h3 = merge(run(ho)+run(ho,DS='-'))
#sv(h3,name)

# Compute locus of PD1 in two parameters
#pd = run(h('PD1'), ICP=[2,4], ISW=2,UZR={},NMX=1000) #NWTN 50 100
# Continue from this label in two parameters
#pd2par = merge(run(pd,UZSTOP={2:4.5})+run(pd,DS='-',UZSTOP={2:2.0}))
#sv(pd2par,name)

#loadbd(name).writeRawFilename('hopf_locus')

#rl(name)
#loadbd(name)(12).writeRawFilename('unstable_periodic1')
#loadbd(name)(15).writeRawFilename('unstable_periodic2')
#loadbd(name)(17).writeRawFilename('unstable_periodic3')
#loadbd(name)(19).writeRawFilename('unstable_periodic4')
#loadbd(name).writeRawFilename('E2_eigs')
plot(name,bifurcation_x=["C"],bifurcation_y=['l1','l2','l3','l4'],miny=-0.3,maxy=0.3,stability=1,use_labels=0,use_symbols=1)
wait()

delete(name)
clean()
