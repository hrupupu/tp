import random
import string
file = 'file.txt'
n = random.randint(256, 512)
N = random.randint(10000, 20000)
with open (file, 'w') as f:
    for i in range(1, N + 1):
        a = string.ascii_letters + string.digits
        st = ''.join(random.sample(a, n)) + '\n'
        f.write(st)
