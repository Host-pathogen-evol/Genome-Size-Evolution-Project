import os, time

def timeConsumingFunction():
    x = 1
    for n in xrange(10000000):
        x += 1


pid = os.fork()

if pid > 0:
    child = pid
else:
    timeConsumingFunction()
    os._exit(0)
t = time.time()
os.waitpid(child, 0)
print time.time() - t
