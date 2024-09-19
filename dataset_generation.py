import numpy as np
from DataGen import DataGen
import time

# Material indices:
# 0-None 1-Ag 2-Al 3-Au 4-Cu 5-GaAs 6-InAs 7-InP 8-Mo 9-Si 10-SiO2

THICKNESS_INC = 2 # Increment in layer thickness.

hosts = ['air', 'wat']

# Bulk dataset generation
print('Begin bulk nanosphere generation')
ti = time.time()
with open('Dataset/data_abs.csv', 'ab') as f: # Destination file can be changed here.
    for host in range(2):
        for m1 in range(1, 11):
            for t1 in range(1, 101, THICKNESS_INC):
                gen = DataGen(m1, t1, hosts[host])
                gen.generate()
                gen.normalise()
                arr = np.array(np.concatenate(((m1,0,t1,0,host), gen.q_abs)), dtype=np.ubyte)
                np.savetxt(f, arr.reshape(1,-1), fmt='%u', delimiter=',')
            print(f'{m1}-{0}-{host} complete.')
ti = time.time() - ti
print(f'Bulk nanosphere generation done. Process took {round(ti)} seconds.')

# Core-shell dataset generation
print('Begin core-shell nanosphere generation')
ti = time.time()
with open('Dataset/data_abs.csv', 'ab') as f: # Destination file can be changed here.
    for host in range(2):
        for m1 in range(1, 11):
            for m2 in range(1, 11):
                if m1 == m2:
                    continue
                td = time.time()
                for t1 in range(1, 101, THICKNESS_INC):
                    for t2 in range(1, 101, THICKNESS_INC):
                        if t1 + t2 > 100:
                            continue
                        gen = DataGen((m1,m2), (t1,t2), hosts[host])
                        gen.generate()
                        gen.normalise()
                        arr = np.array(np.concatenate(((m1,m2,t1,t2,host), gen.q_abs)), dtype=np.ubyte)
                        np.savetxt(f, arr.reshape(1,-1), fmt='%u', delimiter=',')
                print(f'{m1}-{m2}-{host} complete. Took {round(time.time()-td)} seconds.')
ti = time.time() - ti
print(f'Core-shell nanosphere generation done. Process took {round(ti/60)} minutes.')
