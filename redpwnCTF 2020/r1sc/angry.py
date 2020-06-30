import angr

p = angr.Project("r1sc")
good = 0x00401050
bad = 0x0040103b

sm = p.factory.simulation_manager()
print(sm.explore(find=good, avoid=bad))

for f in sm.found:
    print(f.posix.dumps(0))
    print(f.posix.dumps(1))
