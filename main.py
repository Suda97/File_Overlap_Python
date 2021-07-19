def readPrime():
    prime = open("prime.txt", "r")
    pr = []
    for _ in prime:
        line = prime.readline()
        pr.append(line[0:-1])
    print(pr)
    prime.close()
    return pr


def readHappy():
    happy = open("happy.txt", "r")
    ha = []
    for _ in happy:
        line = happy.readline()
        ha.append(line[0:-1])
    print(ha)
    happy.close()
    return ha


if __name__ == '__main__':
    pr = readPrime()
    ha = readHappy()
    sum = []
    for prr in pr:
        if prr in ha:
            sum.append(prr)
    print(sum)
