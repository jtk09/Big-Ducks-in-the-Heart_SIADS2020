# Clear directory - remove junk from previous runs and start fresh
clean()
name = "Luofixedpoints"
delete(name)

# Continue down in Ko with DS<0
l = load(e=name,c="constants",ICP=[2], UZSTOP={2:3.0})
r = run(l)

# Continue down in Ko with DS<0
l = load(r('UZ1'),ICP=[4], UZSTOP={4:[0.000001,1]})
r = merge(run(l)+run(l,DS='-'))
sv(r,name)

# Compute bifurcation diagram with DS>0 and save results
#l = load(e=name,c="constants",ICP=[4], UZSTOP={2:0.000001})
#r = merge(run(l) + run(l,DS='-'))

# Locate and continue periodic orbits from Hopf
#h = load(r('HB1'), ICP=[2,11], ISW=-1, IPS=2)
#h1 = run(h,DS='-')
#ap(h1,name)

# Compute locus of FSNII in two parameters
#b = load(r('BP1'),ICP=[4,2], ISW=2, ILP=0, ISP=0, DSMAX=0.2, NMX=500)
# Continue from this label in two parameters
#bp = merge(run(b, UZSTOP = {2:0.0001}) + run(b, DS='-', UZSTOP = {2:0.0001}))
#bp = merge(run(b) + run(b,DS='-'))
#bp = run(b, UZSTOP = {2:1})
#sv(bp,name)

#loadbd(name).writeRawFilename('2FSN')

plot(name,stability=1,use_labels=0,use_symbols=1)
wait()

delete(name)
clean()
