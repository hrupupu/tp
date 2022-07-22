import random
import string
def line():
        n = random.randint(256, 512)
        return ''.join(random.choices(string.ascii_letters + string.digits, k = n)) + '\n'
def ff():
    file = "test.txt"
    with open (file, 'w') as f:
        for i in range(random.randint(10000, 20000)):
            f.write(line())
ff()
