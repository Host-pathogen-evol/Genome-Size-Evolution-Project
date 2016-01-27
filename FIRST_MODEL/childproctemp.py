import os

pid = os.fork()
if pid > 0:
    fout = open('child.txt', 'w')
    fout.write('File created by child process %d' % pid)
else:
    fout = open('parent.txt', 'w')
    fout.write('File created by parent process')

fout.write('\nEnd of file')
