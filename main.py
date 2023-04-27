import os

if __name__ == "__main__":
    print(os.getcwd())
    rNum = ''
    with open('randoms/Rnumbers.txt', 'r') as f:
        rNum = f.read()
    rNum = int(rNum)
    rNum = str(bin(rNum))
    print("R Numbers:", rNum[2:103])

    csNum = ''
    with open('randoms/c_sharp_random.txt', 'r') as f:
        csNum = f.read()
    csNum = int(csNum)
    csNum = str(bin(csNum))
    print("C Sharp Numbers:", csNum[2:103])