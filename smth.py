import random
import string
def ff():
    def line():
        global res
        n = random.randint(256, 512)
        res = ''.join(random.choices(string.ascii_letters + string.digits, k = n)) + '\n'
    file = "test.txt"
    with open (file, 'w') as f:
        for i in range(random.randint(10000, 20000)):
            line()
            f.write(res)
ff()
