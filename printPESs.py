#!{{python_route}}

import subprocess as sp
from tabulate import tabulate

username = 'uabqut17'

def getIDs(username=username):
    cmd = "sacct --format='JobID,JobName%40,State,AllocCPUS,Partition,NodeList,Elapsed' | grep -v 'g09\|g16\|.bat\|.ext\|CANCELLED\|FAILED\|chemsh\|COMPLETED\|PENDING\|TIMEOUT'"

    stdout = sp.getoutput(cmd).split('\n')[2:]

    IDs = []
    for line in stdout:
        if 'scan' in line:
            IDs.append(line.split()[0])

    return IDs

def printPES(ID):

    cmd = "scontrol show job " + ID + ' | grep WorkDir'
    path =  str(sp.getoutput(cmd))[11:]

    cmd = "scontrol show job " + ID + ' | grep JobName'
    job_name = str(sp.getoutput(cmd))[22:]

    PES = open(path + '/PES.plt', 'r').readlines()

    for l in range(len(PES)):
        PES[l] = str(PES[l])[:-1]
        PES[l] = PES[l].split(', ')


    table = tabulate(PES[1:], headers=PES[0], tablefmt='presto').replace('\n', '\n\t')


    table = '\033[1m' + ID + ' | ' +  job_name + '\033[0m' + ':\n\t' + table + '\n\n'

    return table

def main(IDs):

    print_string = ''
    for ID in IDs:
        print_string += printPES(ID)

    print(print_string)

main(getIDs())

