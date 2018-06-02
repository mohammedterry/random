 #-----random number generator using cellular automata-----
def rule30(a,b,c):
    if int(a) + int(b) + int(c) == 1:
        return '1'
    elif a != b == c == '1':
        return '1'
    return '0'

def cellular_automata(rule, row):
    nextrow = ''
    row = row[-1] + row + row[0]
    for a,b,c in zip(row,  row[1:], row[2:]):
        nextrow += rule(a,b,c)
    return nextrow

def bin2float(binary, bit_len):
    sign,n = [1,-1][int(binary[0])],int(binary[1:],2)
    return sign*n / 2**(bit_len)

def seed(x = 1):
    global seed
    seed = '{0:013b}'.format(x)

def random():
    global seed
    seed = cellular_automata(rule30, seed)
    return bin2float(seed,12)
    
seed()
[print(random()) for _ in range(10)]
