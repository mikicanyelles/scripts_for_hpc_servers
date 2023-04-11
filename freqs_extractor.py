#!{{python_route}}

from sys import argv

file = argv[1]

f = open(file, 'r').readlines()

freqs = []
for line in f:
    if 'frequencies ----' in line:
        for item in line[17:-1].split(' '):
            try :
                float(item)
                freqs.append(item)

            except ValueError:
                pass

print('There are %s frequencies.' % len(freqs))

for freq in freqs:
    if float(freq) < 0:
        print(f'There is an imaginary frequency: {freq} cm^(-1)')

#file_root = file.split('.')[:-1]
file_root = ''

for s in file.split('.')[:-1]:
    file_root = file_root + s

out = open(file_root + '_freqs.txt', 'w')

out.write('\n'.join(freqs))
out.close()

